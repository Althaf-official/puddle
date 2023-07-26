from django.shortcuts import render, redirect
from item.models import Category,Item

from .forms import SignupForm

# Create your views here.
def index(request):
    items =Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()


    return render(request, 'core/index.html',{
        'categories': categories,
        'items':items,
    })

def contact(request):
    return render(request, 'core/contact.html')



def signup(request):
    if request.method == 'POST':
        form =SignupForm(request.POST)
        
        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()


    return render(request, 'core/signup.html',{
        'form':form
    })
"""The code defines a function called signup, which appears to handle the sign-up functionality for a web application.
The function takes a parameter called request. This parameter represents an HTTP request made to the server, usually when a user submits a form on a web page.The function checks if the HTTP request method is "POST". 
In web development, "POST" is commonly used when submitting forms that create or update data on the server.
If the request method is "POST", it means the user has submitted the sign-up form, and the function proceeds to process the form data.
Inside the "POST" block, the code creates an instance of a form called SignupForm and passes the data from the HTTP request (request.POST) to the form.
The is_valid() method is called on the form. This method checks if the data submitted in the form is valid and matches the form's defined validation rules (e.g., required fields, valid email format, etc.).
If the form data is valid (i.e., form.is_valid() returns True), the code saves the form data to the database using the form.save() method. 
This essentially creates a new user account in the backend with the submitted information.
After saving the form data, the function redirects the user to the '/login/' URL using the redirect() function. 
This is a common practice after successful form submissions to take the user to a specific page, in this case, the login page.
If the request method is not "POST" (e.g., "GET"), which means the user is accessing the sign-up page without submitting any data, the code creates an instance of the SignupForm but doesn't process the form data.
In both cases, whether the request method is "POST" or not, the function will render the 'SignupForm' in the context for the template to access it during the rendering of the sign-up page"""