from rest_framework import serializers
from .models import FAQ


class FAQSerializer(serializers.ModelSerializer):
    translations = serializers.SerializerMethodField()

    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer', 'translations']

    def get_translations(self, obj):
        translations = {
            'hi': obj.get_translation('hi'),
            'bn': obj.get_translation('bn'),
        }
        return translations
