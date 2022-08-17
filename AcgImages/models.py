from django.db import models

from .storage import ImageStorage
# Create your models here.
class images(models.Model):
    img = models.ImageField(upload_to='AcgImages',storage=ImageStorage())