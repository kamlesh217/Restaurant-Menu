from django.contrib import admin
from .models import special_item, item, Category

# Register your models here.
admin.site.register(special_item)
admin.site.register(item)
admin.site.register(Category)