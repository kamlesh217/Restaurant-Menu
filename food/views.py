from unicodedata import category
from urllib import request
from django.conf import settings
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.contrib import messages
from .models import item, Category, special_item
# Create your views here.


breakfast_id=Category.objects.get(category_name="breakfast")
lunch_id=Category.objects.get(category_name="lunch")
dinner_id=Category.objects.get(category_name="dinner")

def home(request):
    book(request)
    item_list={
        "breakfast":special_item.objects.get(category=breakfast_id),
        "lunch":special_item.objects.get(category=lunch_id),
        "dinner":special_item.objects.get(category=dinner_id)
    }
    return render(request,'foods/index.html', item_list )


def details_special(request,sitem_id):
    special=special_item.objects.get(id=sitem_id)
    return render(request,'foods/details.html', {"item":special} )


def menu_details(request,item_id):
    Item=item.objects.get(id=item_id)
    return render(request,'foods/details.html', {"item":Item} )


def menu(request):
    Items={'breakfast':item.objects.filter(category=breakfast_id),
    'lunch':item.objects.filter(category=lunch_id),
    'dinner': item.objects.filter(category=dinner_id)
    }
    return render(request,'foods/menu.html', Items )


def contact(request):
    return render(request,'foods/contact.html' )



def admin(request):
    return redirect('admin') 


def book(request):
    if request.method=="POST":
        day=request.POST["day"]
        hour=request.POST["hour"]
        name=request.POST["name"]
        phone=request.POST["phone"]
        person=request.POST["persons"]

        massage=f'day={day}, time={hour}, name={name}, contact={phone}, members={person}'
        print(massage)
        send_mail(
            "for new table booking",
            massage,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=["test@gmail.com"]
        )
        messages.success(request, 'Details has been sent')
        redirect("/food")

def category(request):
    return render(request, "foods/category.html")