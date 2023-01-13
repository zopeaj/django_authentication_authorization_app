from django.db import models
from django.urls import reverse
# Create your models here.

class Product(models.Model):
    id = models.PrimaryKeyField(nullable=False)
    name = models.CharField(default='', nullable=False)
    price = models.FloatField(default=0.0, nullable=False)
    qty = models.IntegerField(default=0, nullable=False)
    discount = models.FloatField(default=0.0, nullable=False)

    def get_absolute_url(self):
        return reverse('product:detail', kwargs={'pk': self.pk})

    def save(self):
        pass

