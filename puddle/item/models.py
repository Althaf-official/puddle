from django.db import models

# Create your models here.
# The Category class is a model in Django with a name attribute of type CharField.
class Category(models.Model):
    name= models.CharField(max_length=255)