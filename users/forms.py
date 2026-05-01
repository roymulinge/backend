from django import forms
from .models import CustomUser

class PhoneNumberForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['phone_number']