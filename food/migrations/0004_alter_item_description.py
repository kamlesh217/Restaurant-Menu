# Generated by Django 4.0.3 on 2022-04-14 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_review_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(max_length=133),
        ),
    ]