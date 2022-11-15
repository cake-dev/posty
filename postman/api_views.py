from functools import wraps
from http import HTTPStatus

from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.cache import never_cache

from .models import Message

never_cache_m = method_decorator(never_cache)


class HttpResponseUnauthorized(HttpResponse):
    status_code = HTTPStatus.UNAUTHORIZED


def auth_required(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return func(request, *args, **kwargs)
        return HttpResponseUnauthorized()
    return wrapper
auth_required_m = method_decorator(auth_required)


class AjaxMixin(object):
    """Common code to Ajax calls."""

    @never_cache_m
    @auth_required_m
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class AjaxUnreadCountView(AjaxMixin, View):
    """Return the number of unread messages for a user."""
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        return JsonResponse({'unread_count': Message.objects.inbox_unread_count(request.user)})
