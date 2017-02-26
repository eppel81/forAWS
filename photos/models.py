from django.db import models


class Photo(models.Model):
    photo = models.ImageField(upload_to='images')
    upload_date = models.DateTimeField(auto_now_add=True)