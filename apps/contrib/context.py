# coding: utf-8
from apps.user.models import UserProfile


def user_info(request):
    if request.user.is_authenticated():
        return {
            'user_info': UserProfile.objects.get(user=request.user)
        }
    return None
