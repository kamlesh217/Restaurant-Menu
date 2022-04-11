from django.shortcuts import render

from food.models import *

def index(request):
    context={
        "gallery":Gallery.objects.all()[:6],
    }
    return render(request, "index.html",context)

def reservation(request):
    return render(request, "reservation.html")

def gallery(request):
    image_list=Gallery.objects.all()
    return render(request, "gallery.html",{"gallery":image_list})

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def menu(request):
    return render(request, "menu.html")