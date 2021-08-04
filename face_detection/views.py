from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import FaceDetection
from pages.models import Image
class FaceDetectionListView(LoginRequiredMixin, generic.ListView):
    template_name = 'face_detection/face_detection_list.html'
    context_object_name = "faces"

    
    def get_queryset(self):
        queryset = FaceDetection.objects.all()
        images = Image.objects.filter(user=self.request.user)
        queryset = [];
        for image in images:
            queryset = FaceDetection.objects.filter(image_fr=image.id)
                

        return queryset
