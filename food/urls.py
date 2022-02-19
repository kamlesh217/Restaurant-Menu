from django.urls import path, include
from food import views
from user import views as v

urlpatterns = [
    path('',views.home, name='home'),
    path('contact/',views.contact, name='contact'),
    path('create_item/',views.create_item, name='admin'),
    path('logout/',v.logout_user, name='logout'),
]


