from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .forms import NewItemForm, EditItemForm
from .models import Item


def items(request):
    query = request.GET.get("query",'')
    items = Item.objects.filter(is_sold=False)

    return render(request, "item/items.html", {
        "items": items,
        'query': query,
        })




def detail(request, pk):  # pk for primary key
    item = get_object_or_404(Item, pk=pk)  # the right pk is from we get the url
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(
        pk=pk
    )[0:3]

    return render(
        request,
        "item/detail.html",
        {
            "item": item,
            "related_items": related_items,
        },
    )


@login_required
def new(request):
    #!handles the processing of form data submitted via a POST request,associates the item with the currently logged-in user, and saves the item to the database.
    if request.method == "POST":
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect("item:detail", pk=item.id)
    else:
        form = NewItemForm()

    return render(
        request,
        "item/form.html",
        {
            "form": form,
            "title": "New Item",
        },
    )


@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == "POST":
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()
            return redirect("item:detail", pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(
        request,
        "item/form.html",
        {
            "form": form,
            "title": "Edit Item",
        },
    )


@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect("dashboard:index")
