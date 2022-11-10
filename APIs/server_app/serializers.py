from rest_framework import serializers
from .models import Staff,Student

class StaffSerializer(serializers.ModelSerializer):
  Staff_id=serializers.ReadOnlyField()
  class Meta:
     model=Staff
     fields="__all__"

class StudentSerializer(serializers.ModelSerializer):
  Student_id=serializers.ReadOnlyField()
  class Meta:
    model=Student
    fields="__all__"