from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse

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

