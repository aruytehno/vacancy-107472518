from django.shortcuts import render

# Create your views here.

import requests
import time
from django.http import JsonResponse
from .models import CurrencyRequest

API_URL = "https://api.exchangerate-api.com/v4/latest/USD"

def get_current_usd(request):
    # Задержка 10 секунд между запросами
    time.sleep(10)

    # Получение данных из API
    response = requests.get(API_URL)
    data = response.json()
    usd_to_rub = data['rates']['RUB']

    # Сохранение в базу данных
    CurrencyRequest.objects.create(usd_to_rub=usd_to_rub)

    # Получение последних 10 запросов
    last_10_requests = CurrencyRequest.objects.order_by('-timestamp')[:10]

    # Формирование ответа
    response_data = {
        'current_usd_to_rub': usd_to_rub,
        'last_10_requests': list(last_10_requests.values())
    }

    return JsonResponse(response_data)
