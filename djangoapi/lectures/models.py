from django.db import models

# Create your models here.

class lecture(models.Model):
    name = models.CharField(max_length=200 )
    language = models.CharField(max_length=200 )
    price = models.CharField(max_length=10 )
    
    def __str__(self) -> str: # From here you can display any value you want in admin dashbord
        return self.name
    