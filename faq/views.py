from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FAQ


class FAQListView(APIView):
    def get(self, request):
        lang = request.GET.get('lang', 'en')
        faqs = FAQ.objects.all()
        data = []
        for faq in faqs:
            translation = faq.get_translation(lang)
            data.append({
                'id': faq.id,
                'question': translation.get('question', faq.question),
                'answer': translation.get('answer', faq.answer)
            })
        return Response(data)
