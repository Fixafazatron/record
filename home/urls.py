from django.urls import path
from .views import index, about, category

urlpatterns = [
    path('', index),
    path('index', index),
    path('about', about),
    path('category', category)
    ]