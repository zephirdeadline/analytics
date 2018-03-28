from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.utils import json

from api.models import Ip


def check_password(func):
    def check(*args, **kwargs):
        try:
            ip = args[0].META['REMOTE_ADDR']
            Ip.objects.get(ip=ip)
            return func(*args, **kwargs)
        except Exception as e:
            return HttpResponse(json.dumps({"error": "You aren't authorized: " + str(e) + " " + args[0].META['REMOTE_ADDR']}), content_type="application/json", status=401)
    return check
