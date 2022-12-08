from django.db import models

# from django.contrib.auth.models import User
from accounts.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    follows = models.ManyToManyField(
        "self", related_name="followed_by", symmetrical=False, blank=True
    )

    def __str__(self):
        return self.user.username


class Post(models.Model):
    user = models.ForeignKey(User, related_name="posts", on_delete=models.DO_NOTHING)
    body = models.CharField(max_length=255)
    image = models.ImageField(
        default="onebyone.png", upload_to="/static/media/images/", blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    post_karma = models.IntegerField(default=0, blank=True, null=True)
    comment_count = models.IntegerField(default=0, blank=True, null=True)
    edited = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.created_at.strftime('%Y-%m-%d')} - {self.body[:30]}"


class Comment(models.Model):
    user = models.ForeignKey(User, related_name="comments", on_delete=models.DO_NOTHING)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    body = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    edited = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.created_at.strftime('%Y-%m-%d')} - {self.body[:30]}"


class Upvoted(models.Model):
    user = models.ForeignKey(User, related_name="upvoted", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="upvoted", on_delete=models.CASCADE)
    upvoted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.user.username} - {self.post.user.username} - {self.post.body[:30]}"
        )


class Downvoted(models.Model):
    user = models.ForeignKey(User, related_name="downvoted", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="downvoted", on_delete=models.CASCADE)
    downvoted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.user.username} - {self.post.user.username} - {self.post.body[:30]}"
        )


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        user_profile.follows.set([instance.profile.id])
        # user_profile.user_karma.set(1)
        user_profile.save()
