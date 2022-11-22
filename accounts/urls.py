from django.urls import path
from .views import SignUpView, EditProfileView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("edit_profile/", EditProfileView.as_view(), name="edit_profile"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
