from django.db import models

# Create your models here.

class Books(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pdate = models.DateField()
    price = models.IntegerField()
    image = models.ImageField()