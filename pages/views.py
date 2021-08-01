from django.db.models import query
from django.views import generic
from django.views.generic import TemplateView
from .forms import ImageForm


class HomePageView(generic.CreateView):
    template_name = 'home.html'
    form_class = ImageForm
    
# class imageView(TemplateView)