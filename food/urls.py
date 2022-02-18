from django.urls import path
from food import views

urlpatterns = [
    #food/
    path('',views.home, name='home'),
    path('contact/',views.contact, name='contact'),
    path('',views.admin, name='admin'),
    #path('',views.food, name='home'),
    #food/item_id
    path('<int:item_id>',views.details, name='detail'),
]