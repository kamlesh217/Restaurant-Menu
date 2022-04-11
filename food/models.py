from django.db import models

# Create your models here.
class Gallery(models.Model):
    gallery_image=models.ImageField( upload_to="gallery/")