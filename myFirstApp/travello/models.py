from django.db import models
from django.utils.timezone import now
import calendar
# Create your models here.

NEWS_CHOICE=[   #PLEASE ADD ACCORDING TO YOUR APPLICATION . I HAVE AN EXAMPLE.
'Sports','Entertaintment','Movies'
]

class Destination(models.Model) :
    name = models.CharField(max_length = 100)
    img = models.ImageField(upload_to = 'pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default = False)
        
class News(models.Model) :
    id = models.IntegerField(default=1)
    img = models.ImageField(uploaded_to='pics')
    date = models.DateTimeField(default=now,editable=False)
   
    headline = models.CharField(max_length = 200, default=News Today)# DEFAULT HEADLINE News Today AN EXAMPLE
    category = models.CharField(max_length = 200,choices=NEWS_CHOICE)
    desc =  models.TextField()
