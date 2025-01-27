from django.db import models

# Create your models here.


class Buyer(models.Model):
    name = models.CharField(max_length=20)
    balance = models.DecimalField(decimal_places=2, max_digits=10000)
    age = models.IntegerField()


class Game(models.Model):
    title = models.CharField(max_length=20)
    cost = models.DecimalField(decimal_places=2, max_digits=1000)
    size = models.DecimalField(decimal_places=4, max_digits=1000)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='buyer')