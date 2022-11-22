# posty/urls.py

from django.urls import path
from .views import dashboard, profile_list, profile
from django.conf import settings
from django.conf.urls.static import static
from .views import dashboard, profile_list, profile, postDetailView, profile_settings
from . import views


app_name = "posty"


urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("post_detail/upvotepost", views.upvote, name="upvote"),
    path("post_detail/deletepost", views.deletePost, name="delete"),
    path("post_detail/updatepost", views.updatePost, name="update"),
    path("post_detail/clearpost", views.clear, name="upvote"),
    path("post_detail/deletecomment", views.deleteComment, name="deletecomment"),
    path("post_detail/updatecomment", views.updateComment, name="updatecomment"),
    path("post_detail/downvotepost", views.downvote, name="downvote"),
    path("post_detail/commentpost", views.comment, name="comment"),
    path("post_detail/<int:pk>/", postDetailView, name="post_detail"),
    path("profile_list/", profile_list, name="profile_list"),
    path("profile/<int:pk>/", profile, name="profile"),
    path("profile_settings/<int:pk>/", profile_settings, name="profile_settings"),
    path("profile_settings/changename", views.changeName, name="changename"),
    path("profile_settings/changeemail", views.changeEmail, name="changeemail"),
    path("profile_settings/changepfp", views.changeProfilePicture, name="changeProfilePicture"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
