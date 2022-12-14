from django.contrib import admin
from . import views
from django.urls import path,include
from .views import StaffViewSet,StudentViewSet
from rest_framework import routers



router=routers.DefaultRouter()
router.register(r'staff',StaffViewSet)
router.register(r'student',StudentViewSet)


urlpatterns = [
    path('',include(router.urls)),
    path('stafflogin/', views.staffLogin),
    path('studentlogin/', views.studentLogin),
    path('getloggedinstaff/', views.getLoggedinstaff),
    path('getloggedinstudent/', views.getLoggedinstudent)
]