from django.urls import path
from food import views

urlpatterns = [
    #food/
    path('',views.home, name='home'),
    #path('',views.food, name='home'),
    #food/item_id
    path('<int:item_id>',views.details, name='detail'),
]