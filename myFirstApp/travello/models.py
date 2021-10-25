from django.db import models
import calendar
# Create your models here.

class Destination(models.Model) :
    name = models.CharField(max_length = 100)
    img = models.ImageField(upload_to = 'pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default = False)
        
class News(models.Model) :
    id : models.IntegerField()
    img : models.ImageField(uploaded_to='pics')
    date : models.DateField()
    month : date.strftime("%B")               #or maybe we can write like: calendar.month_name[date.month] but not sure about this second approach .
    headline : models.CharField(max_length = 200)
    category : models.CharField(max_length = 200)
    desc :  models.TextField()
