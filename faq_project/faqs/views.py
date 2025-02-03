from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FAQ
from .serializers import FAQSerializer
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, "home.html")

# def home(request):
#     return HttpResponse("<h1>Welcome to the FAQ Project</h1><p>Visit <a href='/admin/'>Admin Panel</a> or <a href='/api/faqs/'>API</a>.</p>")

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FAQ
from .serializers import FAQSerializer

class FAQList(APIView):
    def get(self, request):
        lang = request.GET.get('lang', 'en')  # Get the 'lang' parameter from the request, default to 'en'
        faqs = FAQ.objects.all()  # Get all FAQs
        serializer = FAQSerializer(faqs, many=True, context={'lang': lang})  # Pass lang as context to the serializer
        return Response(serializer.data)

