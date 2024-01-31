from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.forms.widgets import PasswordInput, TextInput
from django import forms
from account.models import Account

# - Register/Create a User

class CreateUserForm(UserCreationForm):

    email = forms.EmailField(max_length=225, help_text='Required. Add a valid emaill address')

    class Meta:
        model = Account
        fields = ['email', 'username', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data["email"].lower()
        try:
            account = Account.objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(f'Email {email} is already in use')

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            account = Account.objects.get(username=username)
        except Exception as e:
            return username
        raise forms.ValidationError(f'Username {username} is already in use')
    

# - Login a user

class LoginForm(forms.ModelForm):

    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data["email"]
            password = self.cleaned_data["password"]      
            if not authenticate(email=email, password=password):
                raise forms.ValidationError('Invalid login, please correct your credentials')
     
