from django.db import models

# Create your models here.


class Analytic(models.Model):
    ip = models.CharField(max_length=64)
    ip_server = models.CharField(max_length=64)
    date = models.DateTimeField(auto_now_add=True)
    project = models.CharField(max_length=256)
    text = models.CharField(max_length=256)
    type = models.IntegerField()

    def __str__(self):
        return self.text


class Ip(models.Model):
    ip = models.CharField(max_length=64)

    def __str__(self):
        return self.ip
