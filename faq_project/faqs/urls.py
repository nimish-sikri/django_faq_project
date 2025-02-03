from django.urls import path
from .views import FAQList

urlpatterns = [
    path('faqs/', FAQList.as_view(), name='faq-list'),
]
