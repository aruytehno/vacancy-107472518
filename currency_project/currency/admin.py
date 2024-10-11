from django.contrib import admin
from .models import CurrencyRequest

# Register your models here.

# Регистрация модели CurrencyRequest в админке
admin.site.register(CurrencyRequest)

