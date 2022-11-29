# posty/forms.py

from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm

# from django.contrib.auth.models import User
from accounts.models import User


class PostForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Post something...",
                "class": "textarea is-info is-medium",
                "id": "post-body",
                "maxlength": "255",
                "minlength": "1",
                "rows": "3",
            },
        ),
        label="",
        error_messages={"required": ""},
    )
    image = forms.ImageField(
        required=False,
        widget=forms.widgets.FileInput(
            attrs={
                "class": "is-info",
                "id": "post-image",
                "accept": "image/*",
            }
        ),
        label="",
    )

    class Meta:
        model = Post
        exclude = (
            "user",
            "post_karma",
            "comment_count",
        )


class ProfileChangeForm(forms.ModelForm):

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

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "profile_picture",
        )
        help_texts = {
            "password ": (""),
        }
