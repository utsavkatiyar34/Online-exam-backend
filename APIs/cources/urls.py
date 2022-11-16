from django.contrib import admin
from . import views
from django.urls import path,include
from .views import CourseViewSet,TestViewSet,QuestionViewSet,AssignedViewSet
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'course',CourseViewSet)
router.register(r'test',TestViewSet)
router.register(r'question',QuestionViewSet)
router.register(r'assign',AssignedViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('getcourses/', views.getCourses),
    path('getsubscribed/', views.getassigned),
    path('getassignedtest/', views.getassignedtest),
]