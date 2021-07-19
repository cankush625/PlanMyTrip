from django.db import models

# Create your models here.

class Destination(models.Model) :
    name = models.CharField(max_length = 100)
    img = models.ImageField(upload_to = 'pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default = False)
        
class News() :
    id : int
    img : str
    date : int
    month : str
    headline : str
    category : str
    desc : str