from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Create your views here.
def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')
    else:
        return redirect('/')

def loginuser(request):
    if request.user.is_authenticated:
        return redirect('/create_item')
    else:
        if request.method=='POST':
            username=request.POST['username']
            password=request.POST['password']

            user=authenticate(username=username, password=password)
  
            if user is not None:
                login(request, user)
                return redirect('/create_item')
            else:
                messages.success(request, 'Enter valid details')
                return redirect('/admin')

        return render(request,'user/login.html')
