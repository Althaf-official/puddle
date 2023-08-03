from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404

from item.models import Item


@login_required
def index(request):
    items = Item.objects.filter(created_by=request.user)

    return render(
        request,
        "dashboard/index.html",
        {
            "items": items,
        },
    )
    #!function called index that only allows authenticated users to access the page. It fetches a list of items created by the currently logged-in user and passes that list as context data to an HTML template named "dashboard/index.html". The template can then render the list of items for display on the web page

