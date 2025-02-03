

import logging
from django.db import models
from django.core.cache import cache
from ckeditor.fields import RichTextField
from deep_translator import GoogleTranslator

# Initialize a logger
logger = logging.getLogger(__name__)

class Language(models.Model):
    code = models.CharField(max_length=10, unique=True)  # Language code (e.g., 'hi', 'bn', 'es')
    name = models.CharField(max_length=100)  # Full name of the language (e.g., 'Hindi', 'Bengali')

    def __str__(self):
        return self.name


def translate_text(text, lang):
    """
    Translates text into the target language using GoogleTranslator.
    If the translation returns the same text, a retry is attempted.
    """
    try:
        translated_text = GoogleTranslator(source='auto', target=lang).translate(text)
        # If the translation is identical to the original, try a retry.
        if translated_text.strip().lower() == text.strip().lower():
            # logger.warning(f"Retrying translation for {lang} as output is unchanged.")
            translated_text = GoogleTranslator(source='en', target=lang).translate(text)
        return translated_text
    except Exception as e:
        logger.error(f"Translation error for {lang}: {e}")
        return text  # Fallback to original text if translation fails


class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()

    # JSONField to store translations
    translations = models.JSONField(blank=True, null=True, default=dict)

    # Many-to-Many field to associate languages with this FAQ
    languages = models.ManyToManyField('Language', related_name="faqs", blank=True)

    def __str__(self):
        return self.question

    def get_translated(self, lang='en'):
        """
        Returns a dictionary with the translated question and answer for the requested language.
        Checks the cache first, then the stored translations (JSONField),
        and generates the translation on the fly if missing.
        """
        cache_key = f"faq_{self.id}_{lang}"
        data = cache.get(cache_key)
        if data:
            return data

        if lang == 'en':
            data = {
                'question': self.question,
                'answer': self.answer,
            }
        else:
            if self.translations and lang in self.translations:
                data = self.translations[lang]
            else:
                translated_question = translate_text(self.question, lang)
                translated_answer = translate_text(self.answer, lang)
                data = {
                    'question': translated_question,
                    'answer': translated_answer,
                }
                if self.translations is None:
                    self.translations = {}
                self.translations[lang] = data
                FAQ.objects.filter(pk=self.pk).update(translations=self.translations)
        cache.set(cache_key, data, timeout=3600)
        return data

    def save(self, *args, **kwargs):
        """
        Overrides save() to ensure the default language is added after the object is first saved.
        We avoid calling super().save() twice.
        """
        is_new = self.pk is None  # Check if this is a new object
        super().save(*args, **kwargs)  # Save the object to generate a primary key
        if is_new and not self.languages.exists():
            # Add the default language (English) if no languages are selected.
            # Make sure a Language with code 'en' exists.
            default_language = Language.objects.get(code='en')
            self.languages.add(default_language)

