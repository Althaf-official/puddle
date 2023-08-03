from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .forms import NewItemForm, EditItemForm
from .models import Item, Category

#! this function handles an HTTP request and retrieves a list of unsold items from the database. It also extracts the "query" parameter from the URL's query string and includes it in the template's context. The template "item/items.html" will then use this information to display the list of items and the value of the "query" parameter in the rendered webpage
def items(request):
    query = request.GET.get("query",'')
    category_id = request.GET.get("category",'0')
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)

    if category_id:
        items = items.filter(category_id=category_id)

#! filters the items queryset based on the query value provided. It will update the items queryset to only include objects whose name field contains the query value in a case-insensitive manner when the query variable is truthy (i.e., not empty or None). If query is empty or None, no filtering will be applied, and the original items queryset will remain unchanged.
#?Using Q objects gives you the flexibility to create complex queries and apply complex filter conditions in Django's ORM.
    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, "item/items.html", {
        "items": items,
        'query': query,
        'categories': categories,
        'category_id':int(category_id)
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
