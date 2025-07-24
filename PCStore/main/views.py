from django.http import HttpRequest , HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login , logout

from main.models import *
from store.models import *

def base_view(request):
    
    
    return render(request, "main/base.html", )


def home_view(request):

    pcs = PC.objects.all()[0:3]
    monitors  = Monitor.objects.all()[0:3]
    mouses  = Mouse.objects.all()[0:3]
    chairs  = Chair.objects.all()[0:3]
    headsets  = Headset.objects.all()[0:3]
    keyboards  = Keyboard.objects.all()[0:3]

    return render(request, "main/home.html", {
        "pcs" : pcs , 
        "monitors" : monitors , 
        "mouses" : mouses , 
        "chairs" : chairs,
        "headsets" : headsets,
        "keyboards" : keyboards,
        })



def contact_view(request: HttpRequest):
    
    if request.method == "POST":
        new_contact = Contact(
            first_name=request.POST["first_name"],
            last_name=request.POST["last_name"],
            email=request.POST["email"],
            message=request.POST["message"],

        )
        new_contact.save()
        return redirect('main:contact_messages_view')

    return render(request, "main/contact.html" )

def contact_messages_view(request):

    contacts = Contact.objects.all()


    return render(request, "main/contact_messages.html" , { "contacts" : contacts} )
     
def delete_all_contacts(request):
    Contact.objects.all().delete()
    return redirect("main:contact_messages_view")
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user:
            login(request, user)
            if username == 'admin':
                return render(request, 'main/home.html')
            else:
                return redirect('main:home_view')
        else:
            return render(request, 'main/login.html', {'error': 'Invalid username or password'})
    
    return render(request, 'main/login.html')


def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main:home_view')  
    else:
        form = UserRegistrationForm()

    return render(request, 'main/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('main:home_view')