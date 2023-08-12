from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm,AddRecordForm
from .models import Records

def home(request):

    records = Records.objects.all()

    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        auth = authenticate(request,username=username,password=password)
        if auth is not None:
            login(request,auth)
            messages.success(request,"You have been logged In!")
            return redirect('home')
        else:
            messages.success(request,"There was an error Logging in, Please try again...")
            return redirect('home')
    else:    
        return render(request,'home.html',{'records':records})

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request,"You have been Logged out...")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})

    return render(request, 'register.html', {'form':form})

def update_record(request,id):
    if request.user.is_authenticated:
        customer_records = Records.objects.get(id=id)
        form = AddRecordForm(request.POST or None,instance=customer_records)
        if form.is_valid():
            form.save()
            messages.success(request, "Record updated successfully")
            return redirect('home')
        return render(request, 'update_record.html', {'form':form})
    else:
        messages.success(request, "You must be logged In...")
        return redirect('home')
    
def delete_record(request,id):

    if request.user.is_authenticated:
        delete_it = Records.objects.get(id=id)
        delete_it.delete()
        messages.success(request, "Record deleted successfully")
        return redirect('home')
    else:
        messages.success(request, "You must be logged In...")
        return redirect('home')

def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request,"Record added...")
                return redirect('home')
        return render(request,'add_record.html',{'form':form})
    else:
        messages.success(request, "You must be logged In...")
        return redirect('home')