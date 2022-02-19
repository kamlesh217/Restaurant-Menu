from django.urls import path
from food import views

urlpatterns = [
    path('',views.home, name='home'),
    path('contact/',views.contact, name='contact'),
    path('create_item/',views.create_item, name='admin'),
    #path('add/',views.create_item, name='create_item'),
]


