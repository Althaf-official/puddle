from django.contrib.auth.models import User
from django.db import models

from item.models import Item

class Conversation(models.Model):
    item = models.ForeignKey(Item, related_name="conversations", on_delete=models.CASCADE)
    #!the code creates a Django model named Conversation with a foreign key relationship to the Item model. This allows you to link Conversation instances to specific Item instances in the application's database. 
    members = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('-modified_at',)   

