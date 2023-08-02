from django import forms
from .models import Item

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm): #*subclass of Django's ModelForm class. By inheriting from ModelForm, this form will automatically create form fields based on the model it is associated with.
    class Meta:#?  This is a nested class within NewItemForm that provides additional configuration options for the form.
        model = Item #!This line specifies the model that the form is associated with.
        fields = ("category", "name", "description", "price", "image",)#! fields that should be included in the form

        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),

        }
            #!This configuration allows developers to control the look and feel of form fields in their Django web application by customizing the widget attributes for each form field.