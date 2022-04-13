from django.urls import path, include
from food.views import *


urlpatterns = [
    path('', index , name="homepage"),
    path('reservation', reservation , name="reservation"),
    path('gallery', gallery , name="gallery"),
    path('about', about , name="about"),
    path('menu', menu , name="menu"),
    path('review', review , name="review")
]


