from django.urls import path
from .views import FaceDetectionListView

urlpatterns = [
    path('', FaceDetectionListView.as_view(), name='face_list'),
]
