from django.shortcuts import render
from rest_framework import viewsets
from .models import Staff,Student
from.serializers import StaffSerializer,StudentSerializer

# Staffview
class StaffViewSet(viewsets.ModelViewSet):
    queryset=Staff.objects.all()
    serializer_class=StaffSerializer

#Studentview
class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer