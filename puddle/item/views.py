from django.shortcuts import render,get_object_or_404

from .models import Item

def detail(request, pk):#pk for primary key
    item=get_object_or_404(Item, pk=pk)#the right pk is from we get the url

    return render(request, 'item/detail.html',{
        'item': item
    })


