import mailchimp
from django.conf import settings


def get_mailchimp_api():
    if settings.MAILCHIMP_API_KEY:
        key = settings.MAILCHIMP_API_KEY
    else:
        key = '651886502b1d8d80afdb7065e030cf62-us13'
    return mailchimp.Mailchimp(key)
