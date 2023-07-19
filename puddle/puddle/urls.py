from django.contrib import admin
from django.urls import path

# The code `from core.views import index` is importing the `index` function from the `views` module in
# the `core` package.
# The line `from core.views import index, contact` is importing the `index` and `contact` functions
# from the `views` module in the `core` package. This allows you to use these functions in your code.
from core.views import index,contact


urlpatterns = [
    
    path('',index, name='index'),
    path('contact/',contact,name='contact'),
    path('admin/', admin.site.urls),
]
