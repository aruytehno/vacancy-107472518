from django.contrib import admin
from .models import CurrencyRequest  # Импортируем модель

# Настройка админки для модели CurrencyRequest
@admin.register(CurrencyRequest)
class CurrencyRequestAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'usd_to_rub')  # Поля, которые будут отображаться в таблице
    list_filter = ('timestamp',)  # Добавляет возможность фильтровать записи по дате
    search_fields = ('usd_to_rub',)  # Поле для поиска по курсу доллара
