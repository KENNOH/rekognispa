from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import FaceDetection
from pages.models import Image


class FaceDetectionListView(LoginRequiredMixin, generic.ListView):
    template_name = 'face_detection/face_detection_list.html'
    context_object_name = "faces"


    def get_queryset(self):
        # getting images owned by current user
        images = Image.objects.filter(user=self.request.user)
        # getting face rekognition data using related image in descending order
        queryset = FaceDetection.objects.filter(
            image_fr__in=images).order_by('-image_fr_id')
        return queryset
    
