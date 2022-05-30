from contextlib import nullcontext
from unicodedata import category, name
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 200,null = False,blank = False)
     
    def __str__(self):
          return self.name
      
      
class Pictures(models.Model):
    
    category = models.ForeignKey(category,on_delete=models.SET_NULL)
    image = models.ImageField(null=False,blank=False)
    description = models.CharField(max_length = 300, null= False,blank = False)
    
    def __str__(self):
          return self.description
      
      