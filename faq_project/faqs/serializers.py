from rest_framework import serializers
from .models import FAQ

class FAQSerializer(serializers.ModelSerializer):
    # Override to show translated text
    question_translated = serializers.SerializerMethodField()
    answer_translated = serializers.SerializerMethodField()

    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer', 'question_translated', 'answer_translated']

    def get_question_translated(self, obj):
        """
        Returns the translated question for the given language.
        If the language isn't provided, it defaults to English.
        """
        lang = self.context.get('lang', 'en') 
        return obj.get_translated(lang)['question']

    def get_answer_translated(self, obj):
        """
        Returns the translated answer for the given language.
        If the language isn't provided, it defaults to English.
        """
        lang = self.context.get('lang', 'en')  
        return obj.get_translated(lang)['answer']
