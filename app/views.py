from django.shortcuts import render

# Create your views here.

from app.models import *
from app.serializer import *
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view()

def employeedata(request):
    EQS=Employee.objects.all()
    ejd=EmployeeMS(EQS,many=True)
    return Response(ejd.data)
