from django.shortcuts import render, redirect

from account.forms import CreateUserForm, LoginForm

from django.contrib import auth
from django.contrib.auth import authenticate

from django.contrib import messages

# Create your views here.

# - Register a user

def register(request):
    
    form = CreateUserForm()

    if request.method =='POST':
        
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, "Account created successfully!")
            
            return redirect('account:my_login')
    context = {
        'form' : form
    }

    return render(request, 'account/register.html', context)


#  - Login a user

def my_login(request):

    user = request.user
    
    if user.is_authenticated:
        return redirect('dashboard')

    form = LoginForm()

    if request.POST:
        form = LoginForm(request.POST)

        if form.is_valid():
            email = request.POST['email']
            password = request.POST.get('password')

            user = authenticate(email=email, password=password)

            if user is not None:
                auth.login(request, user)
                messages.success(request, "Login successful")
                if "next" in request.POST:
                    return redirect(request.POST.get("next"))
            
                else:
                    return redirect('dashboard')
    context = {
        'form' : form
    }

    return render(request, 'account/my-login.html', context)



#  - User logout

def user_logout(request):
    
    auth.logout(request)

    messages.success(request, "Logout success!")
            
    return redirect ('account:my_login')
