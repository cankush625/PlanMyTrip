from django.db import models

# Create your models here.



class Destination(models.Model) :
    name = models.CharField(max_length = 100)
    img = models.ImageField(upload_to = 'pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default = False)
        
class News(models.Model) :
    SPORTS='SP'
    ENTERTAINMENT='EN'
    MOVIES='MO'
    NEWS_CHOICE=[   
    (SPORTS,'Sports'),(ENTERTAINMENT,'Entertaintment'),(MOVIES,'Movies'),
    ]
    id = models.IntegerField(null=False)
    img = models.ImageField(uploaded_to='pics')
    date = models.DateTimeField(null=False)
   
    headline = models.CharField(max_length = 200, null=False)
    category = models.CharField(max_length = 200,choices=NEWS_CHOICE,default=SPORTS)
    desc =  models.TextField()
