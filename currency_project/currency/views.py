from django.http import JsonResponse, HttpResponse
from django.core.cache import cache
from datetime import date
from .services import CurrencyService
from .models import ExchangeRate

from django.http import JsonResponse, HttpResponse
from django.core.cache import cache
from datetime import date
from .services import CurrencyService
from .models import ExchangeRate


from django.http import JsonResponse, HttpResponse
from django.core.cache import cache
from datetime import date
from .services import CurrencyService
from .models import ExchangeRate

def get_dollar_rate(request):
    # Попробуем получить курс из кеша
    cached_rate = cache.get('dollar_rate')

    if cached_rate:
        # Если курс есть в кеше, возвращаем его
        return JsonResponse({'usd_to_rub': cached_rate, 'source': 'cache'})

    # Если в кеше нет, запрашиваем через сервис
    rate = CurrencyService.get_exchange_rate()

    if rate:
        # Проверяем, записан ли курс в базу данных
        exchange_rate = ExchangeRate.objects.create(date=date.today(), rate=rate)

        # Кешируем результат на 10 секунд
        cache.set('dollar_rate', rate, timeout=10)

        # Возвращаем полученный курс и указываем источник данных
        return JsonResponse({'usd_to_rub': rate, 'source': 'new_data'})

    else:
        # Если курс не удалось получить, возвращаем сообщение об ошибке
        return HttpResponse("Не удалось получить курс доллара", status=500)


