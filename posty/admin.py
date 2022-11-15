from django.contrib import admin
from django.contrib.auth.models import Group  # , User
from accounts.models import User
from .models import Profile, Post


class ProfileInline(admin.StackedInline):
    model = Profile


class UserAdmin(admin.ModelAdmin):
    model = User
    # only display username field
    fields = ["username", "user_karma"]
    inlines = [ProfileInline]

class CustomPostModelAdmin(admin.ModelAdmin):
    model = Post
    list_display = ["user", "body", "created_at", "post_karma"]


admin.site.unregister(Group)
admin.site.register(Post)
