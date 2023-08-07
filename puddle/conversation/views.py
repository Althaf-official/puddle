from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from item.models import Item

from .forms import ConversationMessageForm
from .models import Conversation

@login_required
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


@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user.id])

    return render(request, "conversation/inbox.html", {
        'conversations':conversations,
        #!{'conversations': conversations}: This is the context data that will be passed to the template. The context data includes a dictionary with a key 'conversations' and a value conversations. The value conversations is likely a queryset or list of conversation objects that will be used to populate the template with relevant data.

    })
    #!this code defines a view function inbox that requires a user to be logged in. It retrieves a list of conversations involving the logged-in user and renders an HTML template to display these conversations in the user's inbox. The @login_required decorator ensures that only authenticated users can access this inbox view.


@login_required
def detail(request, pk):
    conversation = Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)

    if request.method == "POST":
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            conversation.save()

            return redirect('conversation:detail', pk=pk)
    else:
        form = ConversationMessageForm()
        #!The overall purpose of this code snippet is to handle the submission of a form containing conversation message data. It validates the form, associates the message with a conversation and user, saves the data to the database, and redirects the user to a conversation detail page.



    return render(request,'conversation/detail.html',{
        'conversation': conversation,
        'form': form
    })
