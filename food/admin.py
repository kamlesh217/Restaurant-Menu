from django.contrib import admin
from .models import dinner, Lunch, Breakfast 

# Register your models here.
admin.site.register(dinner)
admin.site.register(Lunch)
admin.site.register(Breakfast)