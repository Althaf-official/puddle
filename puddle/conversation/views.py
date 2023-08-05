from django.shortcuts import render, get_object_or_404,redirect


from item.models import Item

from .models import Conversation

def new_conversation(request, item_pk):
    item = get_object_or_404(Item,pk=item_pk)

    if item.created_by == request.user:
        return redirect("dashboard:index")

    conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.id])
    #!this view function handles the process of starting a new conversation related to a specific item. It first checks if the user is not the creator of the item, and then it retrieves the conversations related to the item and involving the user. The returned conversations can be used to display existing conversations to the user or create a new conversation if there are no existing ones.
