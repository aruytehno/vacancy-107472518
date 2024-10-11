from django.db import models

# Create your models here.

class CurrencyRequest(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    usd_to_rub = models.FloatField()

    def __str__(self):
        return f"{self.timestamp}: {self.usd_to_rub}"