from django.db import models

# Create your models here.
class Gallery(models.Model):
    gallery_image=models.ImageField( upload_to="gallery/")

class Item(models.Model):
    category_list=(
        ('B', 'Breakfast'),
        ('L','Lunch'),
        ('D','Dinner')
    )
    title=models.CharField( max_length=100)
    description=models.TextField(max_length=133)
    price=models.FloatField()
    image=models.ImageField(upload_to='Item_folder/')
    category=models.CharField(max_length=1, choices=category_list)


class Review(models.Model):
    name=models.CharField( max_length=50)
    email=models.CharField(null=True, max_length=50)
    phone=models.CharField(null=True, max_length=50)
    massage=models.TextField()
    time=models.DateField(auto_now_add=True)