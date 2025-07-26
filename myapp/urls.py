from django.urls import path
from . import views

urlpatterns = [
     path("dailyportion/", views.dailyportion, name="dailyportion"),
]
