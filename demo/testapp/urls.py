from django.urls import path
from .views import test_app

urlpatterns = [
    path('test_app/', test_app, name='test_app'),  # Ensure correct URL path
]
