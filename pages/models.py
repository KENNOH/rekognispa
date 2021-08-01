from django.db import models


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
