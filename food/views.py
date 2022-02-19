from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from .models import dinner, Lunch, Breakfast
# Create your views here.

def home(request):
    breakfast=Breakfast.objects.all()
    lunch=Lunch.objects.all()
    Dinner=dinner.objects.all()

    con={'breakfast_items':breakfast,
    'lunch_items':lunch,
    'dinner_items': Dinner}

    return render(request,'foods/home.html',con )

def contact(request):
    return render(request,'foods/contact.html' )

def blog(request):
    return render(request,'foods/blog.html' )

def admin(request):
    return redirect('admin') 