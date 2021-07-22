from django.urls import reverse_lazy
from django.views import generic
from .forms import UserProfileCreationForm
from django.views.generic import TemplateView



class HomePageView(TemplateView):
    template_name = 'home.html'
    
class SignUpView(generic.CreateView):
    form_class = UserProfileCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
