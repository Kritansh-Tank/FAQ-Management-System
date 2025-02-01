import pytest
from django.core.cache import cache
from googletrans import Translator
from django_ckeditor_5.fields import CKEditor5Field
from faq.models import FAQ
from django.test import Client
from django.urls import reverse


@pytest.mark.django_db
def test_faq_model_save_and_cache_translations():
    # Arrange
    question = "What is Django?"
    answer = "Django is a high-level Python web framework."

    faq = FAQ(question=question, answer=answer)

    # Act
    faq.save()

    # Assert
    translations = cache.get(f'faq_{faq.id}_translations')
    assert translations is not None, "Translations should be cached after save."
    assert translations.get(
        'question_hi') is not None, "Hindi translation for question should exist."
    assert translations.get(
        'answer_bn') is not None, "Bengali translation for answer should exist."


@pytest.mark.django_db
def test_faq_get_translation_with_cached_data():
    # Arrange
    question = "What is Python?"
    answer = "Python is a versatile programming language."
    faq = FAQ.objects.create(question=question, answer=answer)
    faq.cache_translations()

    # Act
    translation = faq.get_translation('hi')

    # Assert
    assert translation['question'] != question, "Question translation for Hindi should not be identical to original."
    assert translation['answer'] != answer, "Answer translation for Hindi should not be identical to original."


@pytest.mark.django_db
def test_faq_get_translation_without_cached_data():
    # Arrange
    question = "What is AI?"
    answer = "AI stands for Artificial Intelligence."
    faq = FAQ.objects.create(question=question, answer=answer)

    # Clear cache to force translation
    cache.clear()

    # Act
    translation = faq.get_translation('bn')

    # Assert
    assert translation['question'] != question, "Bengali translation for question should not match the original."
    assert translation['answer'] != answer, "Bengali translation for answer should not match the original."


@pytest.mark.django_db
def test_faq_cache_translation_on_update():
    # Arrange
    question = "What is Machine Learning?"
    answer = "Machine Learning enables systems to learn from data."
    faq = FAQ.objects.create(question=question, answer=answer)
    faq.cache_translations()
    new_question = "What is ML?"
    faq.question = new_question

    # Act
    faq.save()
    translations = cache.get(f'faq_{faq.id}_translations')

    # Assert
    assert translations['question_hi'] != question, "Updated Hindi question translation should differ from the old one."
    assert translations['question_hi'] is not None, "New question translation should exist in cache."


@pytest.mark.django_db
def test_api_create_faq(client, django_user_model):
    # Create an admin user for authentication
    admin_user = django_user_model.objects.create_superuser(
        username='admin', password='adminpass', email='admin@example.com'
    )

    # Log in with the admin user
    client.login(username='admin', password='adminpass')

    url = reverse("admin:faq_faq_add")
    data = {
        "question": "What is pytest?",
        "answer": "Pytest is a testing framework for Python."
    }

    # Act
    response = client.post(url, data, follow=True)

    # Assert
    assert response.redirect_chain[-1][1] == 302, "Should redirect after successful submission."
    assert response.status_code == 200, "Final response after redirection should return HTTP 200."
    assert FAQ.objects.filter(question=data['question']).exists(
    ), "FAQ entry should be created in the database."


@pytest.mark.django_db
def test_api_get_faq_list(client):
    # Arrange
    FAQ.objects.create(question="What is caching?",
                       answer="Caching stores data for faster access.")

    url = reverse('faq-list')

    # Act
    response = client.get(url)

    # Assert
    assert response.status_code == 200, "FAQ list API should return HTTP 200."
    assert len(response.json()) > 0, "FAQ list should contain at least one entry."
