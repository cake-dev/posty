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
                "maxlength": "250",
                "minlength": "1",
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
