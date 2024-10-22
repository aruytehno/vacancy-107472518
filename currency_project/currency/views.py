from django.http import JsonResponse, HttpResponse
from django.core.cache import cache
from datetime import datetime
from .services import CurrencyService
from .models import ExchangeRate

def get_dollar_rate(request):
    # Попробуем получить курс из кеша
    cached_rate = cache.get('dollar_rate')

    if cached_rate:
        # Если курс есть в кеше, возвращаем его
        last_requests = cache.get('last_requests', [])
        return JsonResponse({'usd_to_rub': cached_rate, 'source': 'cache', 'last_requests': last_requests})

    # Если в кеше нет, запрашиваем через сервис
    rate = CurrencyService.get_exchange_rate()

    if rate:
        # Проверяем, записан ли курс в базу данных
        ExchangeRate.objects.create(date=datetime.now().date(), rate=rate)

        # Кешируем результат на 10 секунд
        cache.set('dollar_rate', rate, timeout=10)

        # Получаем список последних 10 запросов из кеша
        last_requests = cache.get('last_requests', [])

        # Добавляем новый запрос с датой и временем
        last_requests.append({'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'rate': rate})

        # Оставляем только последние 10 записей
        if len(last_requests) > 10:
            last_requests = last_requests[-10:]

        # Обновляем кеш с новыми данными
        cache.set('last_requests', last_requests, timeout=None)

        # Возвращаем полученный курс и указываем источник данных
        return JsonResponse({'usd_to_rub': rate, 'source': 'new_data', 'last_requests': last_requests})

    else:
        # Если курс не удалось получить, возвращаем сообщение об ошибке
        return HttpResponse("Не удалось получить курс доллара", status=500)
