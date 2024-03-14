from django.urls import path
from word_to_pdf_app import views

urlpatterns = [
    path('',views.home),
]
