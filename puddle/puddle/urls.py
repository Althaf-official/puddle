from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

# The code `from core.views import index` is importing the `index` function from the `views` module in
# the `core` package.
# The line `from core.views import index, contact` is importing the `index` and `contact` functions
# from the `views` module in the `core` package. This allows you to use these functions in your code.
from core.views import index,contact


urlpatterns = [
    
    path('',index, name='index'),
    path('items/', include('item.urls')),
    path('contact/',contact,name='contact'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
