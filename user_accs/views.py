from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserCreationForm
from .models import CustomUser
from django.urls import reverse_lazy


class SignUpView(CreateView):
	form_class = CustomUserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'registration/signup.html'


class ProfileView(LoginRequiredMixin, TemplateView):
	template_name = 'user_accs/profile.html'
	login_url = 'login'