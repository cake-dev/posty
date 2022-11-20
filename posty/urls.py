# posty/urls.py

from django.urls import path
from .views import dashboard, profile_list, profile
from django.conf import settings
from django.conf.urls.static import static
from .views import dashboard, profile_list, profile, postDetailView
from . import views


app_name = "posty"


urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("post_detail/upvotepost", views.upvote, name="upvote"),
    path('post_detail/deletepost', views.deletePost, name='delete'),
    path('post_detail/updatepost', views.updatePost, name='update'),
    path("post_detail/clearpost", views.clear, name="upvote"),
    path("post_detail/downvotepost", views.downvote, name="downvote"),
    path("post_detail/commentpost", views.comment, name="comment"),
    path("post_detail/<int:pk>/", postDetailView, name="post_detail"),
    path("profile_list/", profile_list, name="profile_list"),
    path("profile/<int:pk>/", profile, name="profile"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
