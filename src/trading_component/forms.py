from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import Library_data
User = get_user_model()
class LibraryModelForm(forms.ModelForm):
    class Meta:
        model = Library_data
        fields = (
            'Book_id',
            "description", 
            "create_date", 
            "Book_title",
            "Book_author",
            "Status",
            "Issued_to"  

            
        )
