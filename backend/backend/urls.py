# En tus urls.py
from django.urls import path
from .views import api_test

urlpatterns = [
    path('api/test/', api_test, name='api_test'),
]