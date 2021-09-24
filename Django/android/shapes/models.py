from django.db import models

# Create your models here.
from django.utils import timezone


class Shapes(models.Model):
    description = models.CharField(max_length=1000)
    croptype = models.CharField(max_length=4)
    shapesdescrip = models.CharField(max_length=1000)
    location = models.CharField(max_length=1000)
    update_time = models.CharField(max_length=16)
    left = models.FloatField(max_length=16)
    right = models.FloatField(max_length=16)
    up = models.FloatField(max_length=16)
    down = models.FloatField(max_length=16)
    pic1 = models.ImageField(upload_to="./photos")
    pic2 = models.ImageField(upload_to="./photos", default="")
    pic3 = models.ImageField(upload_to="./photos", default="")
    uploader = models.CharField(max_length=10, default='')
    if_checked = models.BooleanField(default=False)
    id_after_checked = models.IntegerField(default='0')
    area = models.FloatField(max_length=16, default='0.0')

    def __str__(self):
        return self.croptype
