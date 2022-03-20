from django.db import models

# Create your models here.
class Breakfast(models.Model):
    item_name= models.CharField(max_length=200)
    item_desc= models.CharField(max_length=400)
    item_price=models.IntegerField()
    item_image=models.ImageField(upload_to="images/")

    def __str__(self):
        return self.item_name


class Lunch(models.Model):
    item_name= models.CharField(max_length=200)
    item_desc= models.CharField(max_length=400)
    item_price=models.IntegerField()
    item_image=models.ImageField(upload_to="images/")

    def __str__(self):
        return self.item_name

class dinner(models.Model):
    item_name= models.CharField(max_length=200)
    item_desc= models.CharField(max_length=400)
    item_price=models.IntegerField()
    item_image=models.ImageField(upload_to="images/")


    def __str__(self):
        return self.item_name

