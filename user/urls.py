from django.urls import path
from user import views

urlpatterns = [
    path('',views.loginuser, name='login'),
    path('logout/',views.logout_user, name='logout_user'),
    path('category/',views.category, name='category'),
    path('category/dinner/',views.list_dinner, name='list'),
    path('category/breakfast/',views.list_breakfast, name='list'),
    path('category/lunch/',views.list_lunch, name='list'),
    path('<int:item_id>/',views.update_item, name='update_item'),
    path('delete/<int:item_id>/',views.delete_item, name='delete_item'),

]