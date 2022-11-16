from django.shortcuts import render
from rest_framework import viewsets
from .models import Course,Test,Question,Assigned
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from .serializers import CourseSerializer,TestSerializer,QuestionSerializer,AssignedSerializer,SubsSerializer
# Create your views here.


class CourseViewSet(viewsets.ModelViewSet):
    queryset= Course.objects.all()
    serializer_class=CourseSerializer

class TestViewSet(viewsets.ModelViewSet):
    queryset= Test.objects.all()
    serializer_class=TestSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset= Question.objects.all()
    serializer_class=QuestionSerializer

class AssignedViewSet(viewsets.ModelViewSet):
    queryset=Assigned.objects.all()
    serializer_class=AssignedSerializer

@api_view(['Post'])
def getCourses(request):
    request_data = json.load(request)
    author=request_data.get('Author')
    course = Course.objects.filter(Author=author)
    content = CourseSerializer(course, many=True).data
    if content!=[]:
         return Response({"data":content},status=200)
    else:
        return Response({"message":"Invald request"},status=400)

@api_view(['Post'])
def getassigned(request):
    request_data=json.load(request)
    student=request_data.get('Student')
    subscribed=Assigned.objects.filter(Student=student)
    content=SubsSerializer(subscribed, many=True).data
    if content!=[]:
        return Response({"data":content},status=200)
    else:
        return Response({"message":"Invalid request"},status=400)

@api_view(['Post'])
def getassignedtest(request):
    request_data=json.load(request)
    course=request_data.get('Course')
    tests=Test.objects.filter(Course=course)
    content=TestSerializer(tests, many=True).data
    if content!=[]:
        return Response({"data":content},status=200)
    else:
        return Response({"message":"Invalid request"},status=400)