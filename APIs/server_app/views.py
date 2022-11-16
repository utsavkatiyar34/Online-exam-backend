# from argparse import Action
# from http.client import HTTPResponse
import json
# from django.shortcuts import render
from rest_framework import viewsets
# from rest_framework.views import APIView
from .models import Staff,Student
from rest_framework.decorators import api_view,renderer_classes
# from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from.serializers import StaffSerializer,StudentSerializer
# from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import action
from rest_framework.response import Response
# from django.http import JsonResponse


#Staffview
class StaffViewSet(viewsets.ModelViewSet):
    queryset=Staff.objects.all()
    serializer_class=StaffSerializer

#Studentview
class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer


@api_view(['Post'])
def staffLogin(request):
    # print(request["Email"])
    request_data = json.load(request)
    email=request_data.get('Email')
    password=request_data.get('Password')
    user = Staff.objects.filter(Email=email,Password=password,isActive=True)
    content = StaffSerializer(user, many=True).data
    if content!=[]:
         return Response({"Email":email,"Password":password},status=200)
    else:
        return Response({"message":"Invald credentials"},status=400)

@api_view(['POST'])
def studentLogin(request):
    request_data = json.load(request)
    email=request_data.get('Email')
    password=request_data.get('Password')
    user = Student.objects.filter(Email=email,Password=password,isActive=True)
    content = StudentSerializer(user, many=True).data
    if content!=[]:
         return Response({"Email":email,"Password":password},status=200)
    else:
        return Response({"message":"Invald credentials"},status=400)

@api_view(['Post'])
def getLoggedinstaff(request):
    request_data = json.load(request)
    email=request_data.get('Email')
    password=request_data.get('Password')
    user = Staff.objects.filter(Email=email,Password=password,isActive=True)
    content = StaffSerializer(user, many=True).data
    if content!=[]:
         return Response({"data":content},status=200)
    else:
        return Response({"message":"Invald request"},status=400)

@api_view(['Post'])
def getLoggedinstudent(request):
    request_data = json.load(request)
    email=request_data.get('Email')
    password=request_data.get('Password')
    user = Student.objects.filter(Email=email,Password=password,isActive=True)
    content = StudentSerializer(user, many=True).data
    if content!=[]:
         return Response({"data":content},status=200)
    else:
        return Response({"message":"Invald request"},status=400)