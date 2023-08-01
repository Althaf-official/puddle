from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404

from .forms import NewItemForm
from .models import Item

def detail(request, pk):#pk for primary key
    item=get_object_or_404(Item, pk=pk)#the right pk is from we get the url
    related_items =Item.objects.filter(category=item.category,is_sold=False).exclude(pk=pk)[0:3]

    return render(request, 'item/detail.html',{
        'item': item,
        'related_items': related_items,
    })

@login_required
def new(request):
    form = NewItemForm()

    return render(request, "item/form.html", {"form": form})