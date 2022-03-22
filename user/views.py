from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from food.models import item, Category, special_item
from user.forms import ItemForm,specialItemForm



breakfast_id=Category.objects.get(category_name="breakfast")
lunch_id=Category.objects.get(category_name="lunch")
dinner_id=Category.objects.get(category_name="dinner")




# Create your views here.
def logout_user(request):
    logout(request)
    return redirect('/food')




def loginuser(request):
    if request.user.is_authenticated:
        return redirect('/owner/category')
    else:
        if request.method=='POST':
            username=request.POST['username']
            password=request.POST['password']
            print(username, password)

            user=authenticate(username=username, password=password)
            print(user)
            if user is not None:
                print("a")
                login(request, user)
                return redirect('/owner/category')
            else:
                print("b")
                messages.success(request, 'Enter valid details')
                return redirect('/owner')

        return render(request,'user/login.html')




def category(request):
    if request.method=="POST":
        form=ItemForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return redirect("category")
    return render(request,'user/category.html', {"form":ItemForm()})



def list_special(request):
    return render(request,'user/list.html', {"special": special_item.objects.all()})

def list_lunch(request):
    return render(request,'user/list.html', {"lunch": item.objects.filter(category=lunch_id)})

def list_dinner(request):
    return render(request,'user/list.html',{'dinner': item.objects.filter(category=dinner_id)})

def list_breakfast(request):
    return render(request,'user/list.html', {'breakfast':item.objects.filter(category=breakfast_id)})




def update_item(request, item_id):
    Item=item.objects.get(id=item_id)
    if request.method=="POST":
        form=ItemForm(request.POST,request.FILES,instance=Item)
        if form.is_valid():
            form.save()
            return redirect("category")
    return render(request,'user/update.html',{"form":ItemForm(instance=Item)})

def update_special_item(request, item_id):
    Item=special_item.objects.get(id=item_id)
    if request.method=="POST":
        form=specialItemForm(request.POST,request.FILES,instance=Item)
        if form.is_valid():
            form.save()
            return redirect("category")
    return render(request,'user/update.html',{"form":specialItemForm(instance=Item)})





def delete_item(request, item_id):
    Item=item.objects.get(id=item_id)
    Item.delete()
    return redirect("category")