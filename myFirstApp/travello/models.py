from django.db import models

# Create your models here.


class Destination(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to="pics")
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)


class News(models.Model):
    id = models.IntegerField(null=False, blank=False)
    img = models.ImageField(upload_to="pics")
    date = models.DateTimeField(null=False, blank=False)
    headline = models.CharField(max_length=250)
    category = models.CharField(max_length=50)
    desc = models.TextField()
