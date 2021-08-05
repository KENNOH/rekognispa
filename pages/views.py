from django.db.models import query
from django.views import generic
from django.views.generic import TemplateView
from .forms import ImageForm
from .models import Image

class HomePageView(generic.CreateView):
    template_name = 'home.html'
    form_class = ImageForm
    
    def form_valid(self,form):
        # assign current user to image for image ownership
        image = form.save(commit = False)
        image.user = self.request.user
        # image.save()
        return super().form_valid(form)
