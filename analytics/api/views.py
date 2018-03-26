from django.shortcuts import render

# Create your views here.
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Analytic
from api.security import check_password
from rest_object.views import action

# General Rest
#
# class AnalyticSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Analytic
#         fields = ('id', 'name', 'maxspeed')
#
#
# def save_analytic_from_json(request, json, car):
#
#     car.maxspeed = json["maxspeed"]
#     car.name = json["name"]
#     car.save()
#
#
# def analytics(request, id_analytic=None):
#     return action(request, Analytic, AnalyticSerializer, save_analytic_from_json, id_analytic)


@check_password
@api_view(['POST'])
def save(request):
    try:
        analytic = Analytic(project=request.POST['project'],
                            text=request.POST['text'],
                            type=int(request.POST['type']),
                            ip=request.POST['ip'],
                            ip_server=request.META['REMOTE_ADDR'])
        analytic.save()
        return Response({"status": 0})
    except Exception as e:
        return Response({"status": 1, 'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
