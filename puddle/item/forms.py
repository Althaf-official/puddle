from django import forms


from .models import Item

class NewItemForm(forms.ModelForm): #*subclass of Django's ModelForm class. By inheriting from ModelForm, this form will automatically create form fields based on the model it is associated with.
    class Meta:#?  This is a nested class within NewItemForm that provides additional configuration options for the form.
        model = Item #!This line specifies the model that the form is associated with.
        fields = ("category", "name", "description", "price", "image",)#! fields that should be included in the form

