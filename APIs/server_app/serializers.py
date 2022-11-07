from rest_framework import serializers
from .models import Staff,Student

class StaffSerializer(serializers.HyperlinkedModelSerializer):
  Staff_id=serializers.ReadOnlyField()
  class Meta:
     model=Staff
     fields="__all__"

class StudentSerializer(serializers.HyperlinkedModelSerializer):
  Student_id=serializers.ReadOnlyField()
  class Meta:
    model=Student
    fields="__all__"