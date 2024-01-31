# from crmapp import Record
from crmapp.forms import CreateRecordForm, UpdateRecordForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from crmapp.models import Record
from account.models import Account

# - Homepage

def home(request):
    
    return render(request, 'crmapp/index.html')

# - Dashboard

@login_required(login_url='account:my_login')
def dashboard(request):
    context = {}
    user = request.user

    value = 0
    context['value'] = value

    my_records = Record.objects.filter(user=user)
    
    context['records'] = my_records

    if not my_records:
        my_records = None

    return render(request, 'crmapp/dashboard.html', context=context)



# - Create a record

@login_required(login_url='account:my_login')
def create_record(request, *args, **kwargs):

    user_id = kwargs.get('user_id')

    try:
        user = Account.objects.get(id=user_id)

    except Account.DoesNotExist:
        messages.error(request, "User does not exist.")
        return redirect('dashboard')
    
    form = CreateRecordForm()

    if request.method == 'POST':

        form = CreateRecordForm(request.POST)

        if form.is_valid():
            record = form.save(commit=False)
            record.user = user
            record.save()

            messages.success(request, "Your record was created successfully!")

            return redirect('dashboard')
    
    context = {
        'form' : form
    }

    return render(request, 'crmapp/create-record.html', context)



# - Update a record
@login_required(login_url='account:my_login')
def update_record(request, pk):
    
    record = Record.objects.get(id=pk)

    form = UpdateRecordForm(instance=record)

    if request.method == 'POST':

        form = UpdateRecordForm(request.POST, instance=record)
        
        if form.is_valid():

            form.save()

            messages.success(request, "Your record was updated!")
        
            return redirect('dashboard')
    
    context = {
        'form' : form
    }

    return render(request, 'crmapp/update-record.html', context=context)


# - Read / View a singual record

@login_required(login_url='account:my_login')
def signular_record(request, pk):
    
    all_records = Record.objects.get(id=pk)

    context = {
        'record' : all_records
    }
    
    return render(request, 'crmapp/view-record.html', context)



# - Delete a record

@login_required(login_url='my_login')
def delete_record(request, pk):

    record = Record.objects.get(id=pk)

    record.delete()

    messages.success(request, "Your was deleted!")
            
    return redirect('dashboard')