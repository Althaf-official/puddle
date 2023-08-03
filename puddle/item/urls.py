from django.urls import path

from . import views

app_name='item'

urlpatterns =[
    path("new/", views.new, name="new"),
    path('<int:pk>/',views.detail,name='detail'),
    path('<int:pk>/delete/',views.delete,name='delete'),
    path('<int:pk>/edit/',views.edit,name='edit'),
]




"""
urlpatterns: This is a list that stores all the URL patterns for your web application.

path(): It's a function provided by Django that allows you to define a URL pattern. It takes three arguments:

The first argument is the URL pattern, which can contain special placeholders, such as <int:pk>. The pk here is a variable name, 
and <int> indicates that the value passed for this part of the URL should be an integer. 
This is called a path converter and allows you to capture values from the URL and pass them as arguments to the view function.

The second argument is the view function that will be called when a user accesses a URL that matches the defined pattern. 
In this case, the view function is views.detail. When a user accesses a URL like your domain.com/123, 
the detail function in the views.py file will be executed.

The third argument is the optional name parameter, which provides a unique name for the URL pattern. 
This name can be used to reverse the URL later in the code. For example, in templates or views, 
you can refer to the URL pattern by its name instead of hardcoding the URL.

In this specific example, the URL pattern is '<int:pk>', which means it expects an integer value in the URL. 
When a user visits a URL like your domain.com/123, 
Django will capture the integer value 123 and pass it as an argument pk to the detail view function.
"""