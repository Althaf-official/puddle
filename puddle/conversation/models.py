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

class ConversationMessage(models.Model):
    conversation = models.ForeignKey(Conversation, related_name="message", on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_messages',on_delete=models.CASCADE)
    #!on_delete=models.CASCADE specifies the behavior when the referenced User object is deleted. In this case, when a User is deleted, all associated ConversationMessage objects created by that user will also be deleted.
    #!Overall, this ConversationMessage model is designed to store individual messages in a conversation, with each message associated with a specific Conversation and a User who created it. The content field stores the message text, and created_at stores the timestamp when the message was created.