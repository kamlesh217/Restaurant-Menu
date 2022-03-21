from django.db import models

# Create your models here.

class Category(models.Model):
    category_name=models.CharField(max_length=50)

    def __str__(self):
        return self.category_name

class item(models.Model):
    item_name= models.CharField(max_length=200)
    item_full_desc= models.CharField(max_length=400)
    item_sort_desc=models.CharField(max_length=400)
    item_price=models.IntegerField()
    item_image=models.ImageField(upload_to="images/")
    category=models.ForeignKey("Category", on_delete=models.CASCADE)

    def __str__(self):
        return self.item_name

class special_item(models.Model):
    item_name= models.CharField(max_length=200)
    item_desc= models.CharField(max_length=400)
    item_sort_desc=models.CharField(max_length=400)
    item_price=models.IntegerField()
    item_image=models.ImageField(upload_to="images/")
    category=models.ForeignKey("Category", on_delete=models.CASCADE)

    def __str__(self):
        return self.item_name
