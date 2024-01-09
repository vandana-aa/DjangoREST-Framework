from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
# Create your views here.

@api_view(['GET'])
def home(request):
    student_objs=Student.objects.all()
     
    serializer=StudentSerializer(student_objs, many=True)
    return Response({'status':200, 'payload': serializer.data})

@api_view(['POST'])
def post_student(request):
    data=request.data
    serializer=StudentSerializer(data=request.data)
    if not serializer.is_valid():
         print(serializer._errors)
         return Response({'status':403,'errors':serializer._errors,'message':'something went wrong'})
    #print(data)
    serializer.save()
    return Response({'status':200, 'payload':serializer.data, 'message':'you sent'})