from django.db import models

# Create your models here.

class Account(models.Model):
    id = models.PrimaryKeyField(primary_key=True, defaults=random_uuid)
    name = models.CharField(max_length=255)

