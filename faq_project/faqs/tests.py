

import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from .models import FAQ, Language
from django.db import connection


@pytest.fixture
def default_language(db):
    return Language.objects.get_or_create(code='en', defaults={'name': 'English'})[0]

@pytest.fixture
def faq(db, default_language):
    # Clear existing FAQs and reset auto-increment for SQLite
    FAQ.objects.all().delete()
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='faqs_faq';")
    faq_obj = FAQ.objects.create(
        question="What is Django?",
        answer="Django is a high-level Python web framework."
    )
    faq_obj.languages.add(default_language)
    return faq_obj


# ------------------------------
# API Test for FAQ endpoint
# ------------------------------
@pytest.mark.django_db
def test_faq_api_returns_data(faq):
    """
    Test that the FAQ API returns the correct data.
    """
    client = APIClient()
    url = reverse('faq-list')  # Ensure your URL configuration names the FAQ API endpoint as 'faq-list'
    response = client.get(url)
    assert response.status_code == 200
    data = response.json()
    # Check that at least one FAQ in the response contains "Django" in its answer
    assert any("django" in faq_item['answer'].strip().lower() for faq_item in data)


# ------------------------------
# Model Translation Tests
# ------------------------------
@pytest.mark.django_db
def test_hindi_translation(faq):
    """
    Test that the Hindi translation is different from the original content.
    """
    translated = faq.get_translated('hi')
    # Compare in a case-insensitive way after stripping whitespace
    assert translated['question'].strip().lower() != faq.question.strip().lower(), "Hindi translation failed: question is identical."
    assert translated['answer'].strip().lower() != faq.answer.strip().lower(), "Hindi translation failed: answer is identical."
    print("Hindi Question:", translated['question'])
    print("Hindi Answer:", translated['answer'])


@pytest.mark.django_db
def test_bengali_translation(faq):
    """
    Test that the Bengali translation is different from the original content.
    """
    translated = faq.get_translated('bn')
    assert translated['question'].strip().lower() != faq.question.strip().lower(), "Bengali translation failed: question is identical."
    assert translated['answer'].strip().lower() != faq.answer.strip().lower(), "Bengali translation failed: answer is identical."
    print("Bengali Question:", translated['question'])
    print("Bengali Answer:", translated['answer'])


@pytest.mark.django_db
def test_german_translation(faq):
    """
    Test that the German translation is different from the original content.
    Note: German language code should be 'de'.
    """
    translated = faq.get_translated('de')
    print("German Question:", translated['question'])
    print("German Answer:", translated['answer'])
    assert translated['question'].strip().lower() != faq.question.strip().lower(), "German translation failed: question is identical."


@pytest.mark.django_db
def test_french_translation(faq):
    """
    Test that the French translation is different from the original content.
    """
    translated = faq.get_translated('fr')
    print("French Question:", translated['question'])
    print("French Answer:", translated['answer'])
    assert translated['question'].strip().lower() != faq.question.strip().lower(), "French translation failed: question is identical."


@pytest.mark.django_db
def test_italian_translation(faq):
    """
    Test that the French translation is different from the original content.
    """
    translated = faq.get_translated('it')
    print("Italian Question:", translated['question'])
    print("Italian Answer:", translated['answer'])
    assert translated['question'].strip().lower() != faq.question.strip().lower(), "Italian translation failed: question is identical."
