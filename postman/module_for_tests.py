"""
Utilities for tests.py usage.

"""

from django.conf import settings
from django.core.mail import send_mail


class UserRepresentation:
    "for POSTMAN_SHOW_USER_AS, in test_get_user_representation()"
    def __init__(self, user):
        self.user = user

    def __str__(self):
        return user_representation(self.user)


def user_representation(user):
    "for POSTMAN_SHOW_USER_AS, in test_get_user_representation()"
    return 'nick_' + user.get_username()  # some user representation

def from_email(context):
    "for POSTMAN_FROM_EMAIL, in test_from_email()"
    return '{}_{}@domain.tld'.format(
        context['object'].sender.username,
        context['action']
    )  # a way to prove at the same time the parameters transmission

def params_email(context):
    "for POSTMAN_PARAMS_EMAIL, in test_params_email()"
    return {
        'reply_to': ['{}@domain.tld'.format(context['object'].sender.username)],
        'headers': {'X-my-choice': context['action']}
    }  # a way to prove at the same time the parameters transmission

def notification_approval(user, action, site):
    "for POSTMAN_NOTIFICATION_APPROVAL, in test_notification_approval()"
    return '{}_{}@domain.tld'.format(user.username, action)  # a way to prove at the same time the parameters transmission

def send(users, label, extra_context):
    "for POSTMAN_NOTIFIER_APP = 'postman.module_for_tests'"
    send_mail('subject', 'message', settings.DEFAULT_FROM_EMAIL, [users[0].email])