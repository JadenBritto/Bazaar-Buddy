from django.urls import path
from . import views

urlpatterns = [
    path('ping/', views.ping, name='ping'),
    path('generate-ai-report/', views.generate_ai_report, name='generate_ai_report'),
]