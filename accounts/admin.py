# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ["username", "email", "user_karma", "profile_picture"]
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("user_karma",)}),
        (None, {"fields": ("profile_picture",)}),
    )


admin.site.register(User, CustomUserAdmin)
