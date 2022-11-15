from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    user_karma = models.IntegerField(default=0, blank=True, null=True)

    profile_picture = models.ImageField(
        default="default_pfp.jpg", upload_to="images/", blank=True, null=True
    )

    class Meta:
        db_table = "auth_user"
