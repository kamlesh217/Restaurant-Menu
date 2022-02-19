from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from .models import Items
# Create your views here.

def home(request):
    return render(request,'foods/home.html' )

def contact(request):
    return render(request,'foods/contact.html' )

def blog(request):
    return render(request,'foods/blog.html' )

def admin(request):
    return redirect('admin')

def food(request):
    obj=Items.objects.all()
    con={
        "item_list":obj,
    }
    return render(request,'foods/navbar.html', con )

def details(request, item_id):
    item=Items.objects.get(pk=item_id)
    con={
        'items':item,
    }
    return render(request,'foods/details.html', con )  