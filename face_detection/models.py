from django.db import models
from pages.models import Image
# Create your models here.


class FaceDetection(models.Model):
    imageURL = models.URLField(max_length=256)
    gender = models.CharField(max_length=16)
    age_low = models.IntegerField(blank=True, null=True)
    age_high = models.IntegerField(blank=True, null=True)
    emotion = models.CharField(max_length=64)
    feature = models.CharField(max_length=64)