from django.db import models

# Create your models here.

class RussellData(models.Model):
    TICKER = models.CharField(max_length=10)
    DATE = models.DateField()
    OPEN = models.DecimalField(max_digits=5, decimal_places=2)
    HIGH = models.DecimalField(max_digits=5, decimal_places=2)
    LOW = models.DecimalField(max_digits=5, decimal_places=2)
    CLOSE = models.DecimalField(max_digits=5, decimal_places=2)
    ADJ_CLOSE = models.DecimalField(max_digits=5, decimal_places=2)
    VOLUME = models.IntegerField(max_length=15)