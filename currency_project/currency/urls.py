from django.urls import path
from . import views

urlpatterns = [
    path('get-current-usd/', views.get_dollar_rate, name='get_current_usd'),  # Исправили на существующую функцию
]