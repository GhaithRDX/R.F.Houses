from typing import Type
from django.db import models
from django.db.models.options import Options

# Create your models here.

class House(models.Model):
    state = models.CharField(max_length=50)
    area = models.IntegerField()
    price = models.IntegerField()
    city = models.CharField(max_length=50)
    is_available = models.BooleanField()
    views = models.IntegerField()
    description = models.CharField(max_length=1000)
    file =  models.ImageField(upload_to='images/')
    id = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.id
        