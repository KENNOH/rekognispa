from django.db import models
from django.db.models.signals import post_save
from face_detection.services import show_faces
import os


class Image(models.Model):
    RECOGNITION_TYPES = (
        ('FACE', 'Face Rekognition'),
        ('OBJECT', 'Object Rekognition'),
        ('TEXT', 'Text Rekognition'),
    )

    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
    rekognition_type = models.CharField(
        max_length=6,
        choices=RECOGNITION_TYPES,
        default=None
    )

    def __str__(self):
        return f"{self.title} in {self.rekognition_type}"


def save_image(sender, instance, created, **kwargs):
    photo, bucket = instance.image.name, os.environ.get('S3_BUCKET_NAME')
    if instance.rekognition_type == 'FACE':
        faceDetails = show_faces(photo, bucket)
        print(faceDetails)


post_save.connect(save_image, sender=Image)
