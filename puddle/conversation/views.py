from django.shortcuts import render, get_object_or_404, redirect


from item.models import Item

from .forms import ConversationMessageForm
from .models import Conversation


def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)

    if item.created_by == request.user:
        return redirect("dashboard:index")

    conversations = Conversation.objects.filter(item=item).filter(
        members__in=[request.user.id]
    )

    if conversations:
        pass  # redirect to conversation

    if request.method == "POST":
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('item:detail', pk=item_pk)
    else:
        form = ConversationMessageForm()

    return render(request, "conversation/new.html", {
        "form": form
    })
#!this view function is responsible for handling the creation of a new conversation related to a specific item and processing the form data to save the conversation message. It also checks for existing conversations and redirects to the appropriate URL if needed.
