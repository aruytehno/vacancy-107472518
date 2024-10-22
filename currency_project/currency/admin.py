from django.contrib import admin
from .models import ExchangeRate  # Импортируем новую модель

# Настройка админки для модели ExchangeRate
@admin.register(ExchangeRate)
class ExchangeRateAdmin(admin.ModelAdmin):
    list_display = ('date', 'rate')  # Поля, которые будут отображаться в таблице
    list_filter = ('date',)  # Фильтрация записей по дате
    search_fields = ('rate',)  # Поле для поиска по курсу
