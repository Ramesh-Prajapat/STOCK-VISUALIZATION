from django.db import models

# Create your models here.

class RussellData(models.Model):
    TICKER = models.CharField(max_length=20)
    D_DATE = models.DateField()
    OPEN = models.DecimalField(max_digits=15, decimal_places=5)
    HIGH = models.DecimalField(max_digits=15, decimal_places=5)
    LOW = models.DecimalField(max_digits=15, decimal_places=5)
    CLOSE = models.DecimalField(max_digits=15, decimal_places=5)
    ADJ_CLOSE = models.DecimalField(max_digits=15, decimal_places=5)
    VOLUME = models.IntegerField(max_length=15)