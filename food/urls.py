from django.urls import path, include
from food import views
from user import views as v

urlpatterns = [
    path('',views.home, name='home'),
    path('menu/',views.menu, name='menu'),
     path('book/',views.book, name='book'),
    path('contact/',views.contact, name='contact'),
    path('<int:sitem_id>/',views.details_special, name='details_special'),
    path('details/<int:item_id>/',views.menu_details, name='menu_details'),
]


