from django.db import models
from django.core.cache import cache
from googletrans import Translator
from django_ckeditor_5.fields import CKEditor5Field

translator = Translator()


class FAQ(models.Model):
    question = models.TextField()
    answer = CKEditor5Field()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.cache_translations()

    def cache_translations(self):
        languages = ['hi', 'bn']
        translations = {}
        for lang in languages:
            translations[f'question_{lang}'] = translator.translate(
                self.question, dest=lang).text
            translations[f'answer_{lang}'] = translator.translate(
                self.answer, dest=lang).text
        cache.set(
            f'faq_{self.id}_translations',
            translations,
            timeout=86400,  # Cache for 24 hours
        )

    def get_translation(self, lang):
        cached_translations = cache.get(f'faq_{self.id}_translations')
        if not cached_translations:
            self.cache_translations()
            cached_translations = cache.get(f'faq_{self.id}_translations')
        return {
            'question': cached_translations.get(
                f'question_{lang}', self.question
            ),
            'answer': cached_translations.get(
                f'answer_{lang}', self.answer
            )
        }
