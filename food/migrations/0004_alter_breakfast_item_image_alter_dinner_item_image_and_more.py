# Generated by Django 4.0.1 on 2022-02-19 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_alter_breakfast_item_image_alter_dinner_item_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breakfast',
            name='item_image',
            field=models.CharField(default='https://thumbs.dreamstime.com/z/food-lettering-typography-word-hot-made-red-spicy-chili-peppers-green-background-mexican-italian-spanish-greek-cuisine-120260831.jpg', max_length=500),
        ),
        migrations.AlterField(
            model_name='dinner',
            name='item_image',
            field=models.CharField(default='https://thumbs.dreamstime.com/z/food-lettering-typography-word-hot-made-red-spicy-chili-peppers-green-background-mexican-italian-spanish-greek-cuisine-120260831.jpg', max_length=500),
        ),
        migrations.AlterField(
            model_name='lunch',
            name='item_image',
            field=models.CharField(default='https://thumbs.dreamstime.com/z/food-lettering-typography-word-hot-made-red-spicy-chili-peppers-green-background-mexican-italian-spanish-greek-cuisine-120260831.jpg', max_length=500),
        ),
    ]