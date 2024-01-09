from rest_framework import serializers
from .models import *
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        #fields=['name','age']
        # exclude=['id',] will serialize everything except id
        fields='__all__'
