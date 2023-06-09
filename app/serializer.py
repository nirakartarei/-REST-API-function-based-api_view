from app.models import *
from rest_framework import serializers


class EmployeeMS(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'