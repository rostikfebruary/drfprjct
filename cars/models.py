from django.db import models


class NewCar(models.Model):
    class Meta:
        db_table = 'cars'
    brand = models.CharField(max_length=60)
    price = models.IntegerField(default=0)
    year = models.IntegerField(default=0)
    v = models.FloatField(default=0)