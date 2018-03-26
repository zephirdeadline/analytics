from django.contrib import admin

# Register your models here.
from api.models import Ip, Analytic

admin.site.register(Ip)
admin.site.register(Analytic)