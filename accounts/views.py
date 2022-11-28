from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .models import User

from .forms import CustomUserCreationForm, CustomUserChangeForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("posty:dashboard")
    template_name = "registration/signup.html"


class EditProfileView(UpdateView):
    model = User
    form_class = CustomUserChangeForm
    success_url = reverse_lazy("posty:dashboard")
    template_name = "registration/edit_profile.html"
    # save form if valid
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
