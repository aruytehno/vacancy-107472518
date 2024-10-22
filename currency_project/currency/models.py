from django.db import models

# Модель для хранения курсов обмена валют
class ExchangeRate(models.Model):
    date = models.DateField()  # Поле для хранения даты
    rate = models.DecimalField(max_digits=10, decimal_places=4)  # DecimalField для точного хранения курса

    def __str__(self):
        return f"{self.date}: {self.rate}"  # Удобное отображение данных в виде строки
