from django.shortcuts import render, redirect
from .models import Post, Profile, Upvoted, Downvoted, Comment
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from accounts.models import User


@login_required
def dashboard(request):
    # form = PostForm(request.POST or None)
    # if request.method == "POST":
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
        img = form.cleaned_data["image"]
        body = form.cleaned_data["body"]
        if img is None:
            img = "images/onebyone.png"
        post = Post.objects.create(user=request.user, image=img, body=body)
        post.save()
        return redirect("posty:dashboard")

    sorting = request.GET.get("sort")
    ordering = {
        "date_sort": "-created_at",
        "karma_sort": "-post_karma",
        "comment_sort": "-comment_count",
        None: "-created_at",
    }
    # followed_posts = Post.objects.filter(
    #     user__profile__in=request.user.profile.follows.all()
    # ).order_by("-created_at")

    followed_posts = Post.objects.filter(
        user__profile__in=request.user.profile.follows.all()
    ).order_by(ordering[sorting])

    return render(
        request,
        "posty/dashboard.html",
        {"form": form, "posts": followed_posts, "comment": Comment},
    )


def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, "posty/profile_list.html", {"profiles": profiles})


def profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    profile.user.posts.order_by("-created_at")
    return render(request, "posty/profile.html", {"profile": profile})


def postDetailView(request, pk):
    post = Post.objects.get(pk=pk)
    return render(
        request,
        "posty/post_detail.html",
        {"post": post, "comment": Comment.objects.filter(post=post)},
    )


def upvote(request):
    if request.method == "GET":
        post_id = request.GET["post_id"]
        user_id = request.GET["user_id"]
        post = Post.objects.get(pk=post_id)
        user = User.objects.get(pk=user_id)
        if user_id == post.user.id:
            return HttpResponse("You can't upvote your own post!")
        elif (
            Upvoted.objects.filter(user=user).exists()
            and Upvoted.objects.filter(post=post).exists()
        ):
            return HttpResponse("You have already upvoted this post!")
        else:
            if (
                Downvoted.objects.filter(user=user).exists()
                and Downvoted.objects.filter(post=post).exists()
            ):
                Downvoted.objects.filter(user=user, post=post).delete()
                post.post_karma += 2
                user.user_karma += 2
            else:
                post.post_karma += 1
                user.user_karma += 1
            post.save()
            user.save()
            upvoted = Upvoted(user=user, post=post)
            upvoted.save()
            return HttpResponse("Success!")
    else:
        return HttpResponse("Request method is not a GET")


def clear(request):
    if request.method == "GET":
        post_id = request.GET["post_id"]
        user_id = request.GET["user_id"]
        post = Post.objects.get(pk=post_id)
        user = User.objects.get(pk=user_id)
        if (
            Upvoted.objects.filter(user=user).exists()
            and Upvoted.objects.filter(post=post).exists()
        ):
            Upvoted.objects.filter(user=user, post=post).delete()
            post.post_karma -= 1
            user.user_karma -= 1
        elif (
            Downvoted.objects.filter(user=user).exists()
            and Downvoted.objects.filter(post=post).exists()
        ):
            Downvoted.objects.filter(user=user, post=post).delete()
            post.post_karma += 1
            user.user_karma += 1
        post.save()
        user.save()
        return HttpResponse("Success!")
    else:
        return HttpResponse("Request method is not a GET")


def downvote(request):
    if request.method == "GET":
        post_id = request.GET["post_id"]
        user_id = request.GET["user_id"]
        post = Post.objects.get(pk=post_id)
        user = User.objects.get(pk=user_id)
        if user_id == post.user.id:
            return HttpResponse("You can't downvote your own post!")
        elif (
            Downvoted.objects.filter(user=user).exists()
            and Downvoted.objects.filter(post=post).exists()
        ):
            return HttpResponse("You have already downvoted this post!")
        else:
            if (
                Upvoted.objects.filter(user=user).exists()
                and Upvoted.objects.filter(post=post).exists()
            ):
                Upvoted.objects.filter(user=user).delete()
                post.post_karma -= 2
                user.user_karma -= 2
            else:
                post.post_karma -= 1
                user.user_karma -= 1
            post.save()
            user.save()
            downvoted = Downvoted(user=user, post=post)
            downvoted.save()
            return HttpResponse("Success!")
    else:
        return HttpResponse("Request method is not a GET")


def comment(request):
    if request.method == "GET":
        post_id = request.GET["post_id"]
        user_id = request.GET["user_id"]
        comment = request.GET["comment"]
        post = Post.objects.get(pk=post_id)
        post.comment_count += 1
        user = User.objects.get(pk=user_id)
        comment = Comment(user=user, post=post, body=comment)
        comment.save()
        post.save()
        return HttpResponse("Success!")
    else:
        return HttpResponse("Request method is not a GET")


def deletePost(request):
    if request.method == "GET":
        post_id = request.GET["post_id"]
        user_id = int(request.GET["user_id"])
        post = Post.objects.get(pk=post_id)
        # user = User.objects.get(pk=user_id)

        if post.user.id == user_id:
            print("Success!")
            post.delete()
            return redirect("posty:dashboard")
        else:
            return HttpResponse("You can't delete this post!")
    else:
        return HttpResponse("Request method is not a GET")
