from django.urls import path
from food import views

urlpatterns = [
    #food/
    path('',views.home, name='home'),
    path('contact/',views.contact, name='contact'),
    path('blog/',views.blog, name='blog'),
    path('admin/',views.admin, name='admin'),
    #food/item_id
]


