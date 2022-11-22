from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = (
            "username",
            "email",
            "profile_picture",
        )


class CustomUserChangeForm(UserChangeForm):

    # fields for changing profile values
    username = forms.CharField(
        required=False,
        widget=forms.widgets.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "input is-info is-medium",
                "id": "username",
                "maxlength": "25",
                "minlength": "1",
            }
        ),
        label="",
        error_messages={"required": ""},
    )
    email = forms.EmailField(
        required=False,
        widget=forms.widgets.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "input is-info is-medium",
                "id": "email",
                "maxlength": "50",
                "minlength": "1",
            }
        ),
        label="",
        error_messages={"required": ""},
    )
    # field to change profile picture
    profile_picture = forms.ImageField(
        required=False,
        widget=forms.widgets.FileInput(
            attrs={
                "class": "is-info",
                "id": "profile-picture",
                "accept": "image/*",
            }
        ),
        label="",
    )

    # logic to apply changes to profile
    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data["username"]
        user.email = self.cleaned_data["email"]
        user.profile_picture = self.cleaned_data["profile_picture"]
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "profile_picture",
        )
