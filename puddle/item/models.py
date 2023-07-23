from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# The Category class is a model in Django with a name attribute of type CharField.
class Category(models.Model):
    name= models.CharField(max_length=255)

    class meta:
        ordering = ('name',)
        verbose_name_plural='Categories'

    def __str__(self) -> str:
        return self.name
    
class Item(models.Model):
    category =models.ForeignKey(Category,related_name='items', on_delete=models.CASCADE)#when we delete category it will delete all items also
    name= models.CharField(max_length=255)
    description=models.TextField(blank=True,null=True)
    price= models.FloatField()
    image =models.ImageField(upload_to='item_images',blank=True,null=True)
    is_sold =models.BooleanField(default=False)
    created_by=models.ForeignKey(User,related_name='items',on_delete=models.CASCADE)
    created_at =models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name