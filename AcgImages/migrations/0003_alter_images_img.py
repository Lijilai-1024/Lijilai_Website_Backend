# Generated by Django 3.2.11 on 2022-08-17 22:17

import AcgImages.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AcgImages', '0002_alter_images_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='img',
            field=models.ImageField(storage=AcgImages.storage.ImageStorage(), upload_to='AcgImages'),
        ),
    ]
