from django import VERSION
from django.conf import settings
if VERSION < (2, 0):
    from django.conf.urls import url as re_path
else:
    from django.urls import re_path
if getattr(settings, 'POSTMAN_I18N_URLS', False):
    from django.utils.translation import pgettext_lazy
else:
    def pgettext_lazy(c, m): return m

from .api_views import AjaxUnreadCountView

app_name = 'api'
urlpatterns = [
    re_path(pgettext_lazy('postman_url', r'^unread-count/$'), AjaxUnreadCountView.as_view(), name='unread-count'),
]
