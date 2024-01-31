from django.forms.widgets import PasswordInput, TextInput
from django import forms
from crmapp.models import Record


# - Create a record form

class CreateRecordForm(forms.ModelForm):

    class Meta:
        model = Record
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'lga' ,'country', 'gender' ]



# - Udpate a record form

class UpdateRecordForm(forms.ModelForm):

    class Meta:
        model = Record
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'lga' ,'country', 'gender' ]
