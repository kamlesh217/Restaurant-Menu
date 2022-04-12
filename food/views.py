from cmath import exp
from multiprocessing import context
from unicodedata import category
from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail
from food.models import *

def index(request):
    context={
        "gallery":Gallery.objects.all()[:6],
    }
    return render(request, "index.html",context)

def reservation(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        member=request.POST['person']
        number=request.POST['phone']
        date=request.POST['date']
        details=f"name={name} \n, date={date},\n perosns={member},\n contact={number}//{email}"
        try:
            subject = 'booking details'
            message = details
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['Test@gmail.com', ]
            send_mail( subject, message, email_from, recipient_list )
        except:
            print(details)

    return render(request, "reservation.html")

def gallery(request):
    image_list=Gallery.objects.all()
    return render(request, "gallery.html",{"gallery":image_list})

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def menu(request):
    context={
        'All_item':Item.objects.all(),
        'Breakfast':Item.objects.filter(category='B'),
        'Lunch':Item.objects.filter(category='L'),
        'Dinner':Item.objects.filter(category='D'),
    }
    return render(request, "menu.html",context)