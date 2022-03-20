from django.conf import settings
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from .models import dinner, Lunch, Breakfast
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.

def home(request):
    breakfast=Breakfast.objects.all()
    lunch=Lunch.objects.all()
    Dinner=dinner.objects.all()

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
        redirect("/home")
        


    con={'breakfast_items':breakfast,
    'lunch_items':lunch,
    'dinner_items': Dinner,
    }

    return render(request,'foods/home.html',con )

def contact(request):
    return render(request,'foods/contact.html' )


def create_item(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            name=request.POST['name']
            type=request.POST['type']
            des=request.POST['desc']
            price=request.POST['price']
            image=request.POST['image']

            if type=='lunch':
                if image=='':
                    lunch_obj=Lunch(item_name=name, item_desc=des, item_price=price)
                    lunch_obj.save()

                else:
                    lunch_obj=Lunch(item_name=name, item_desc=des, item_price=price, item_image=image)
                    lunch_obj.save()

            elif type=='dinner':
                if image=='':
                    dinner_obj=dinner(item_name=name, item_desc=des, item_price=price)
                    dinner_obj.save()

                else:
                    dinner_obj=dinner(item_name=name, item_desc=des, item_price=price, item_image=image)
                    dinner_obj.save()
          
        
            elif type=='breakfast':
                if image=='':
                    breakfast_obj=Breakfast(item_name=name, item_desc=des, item_price=price)
                    breakfast_obj.save()
             

                else:
                    breakfast_obj=Breakfast(item_name=name, item_desc=des, item_price=price, item_image=image)
                    breakfast_obj.save()
        return render(request,'foods/item.html' )
    else:
        return redirect('/')



def admin(request):
    return redirect('admin') 


    

    