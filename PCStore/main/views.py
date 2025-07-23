from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse

from main.models import *
from store.models import *


def base_view(request):
    
    
    return render(request, "main/base.html", )


def admin_base_view(request):
    
    
    return render(request, "main/admin_base.html", )

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


def admin_home_view(request):

    pcs = PC.objects.all()[0:3]
    monitors  = Monitor.objects.all()[0:3]
    mouses  = Mouse.objects.all()[0:3]
    chairs  = Chair.objects.all()[0:3]
    headsets  = Headset.objects.all()[0:3]
    keyboards  = Keyboard.objects.all()[0:3]

    return render(request, "main/admin_home.html", {
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
     
