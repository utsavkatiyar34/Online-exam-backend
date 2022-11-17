from rest_framework import serializers
from .models import Course,Test,Question,Assigned,Score

class CourseSerializer(serializers.ModelSerializer):
    Course_id=serializers.ReadOnlyField()
    
    class Meta:
        model=Course
        fields="__all__"

class TestSerializer(serializers.ModelSerializer):
    Test_id=serializers.ReadOnlyField()
    
    class Meta:
        model=Test
        fields="__all__"

class QuestionSerializer(serializers.ModelSerializer):
    Test_id=serializers.ReadOnlyField()
    
    class Meta:
        model=Question
        fields="__all__"

class AssignedSerializer(serializers.ModelSerializer):
    id=serializers.ReadOnlyField()

    class Meta:
        model=Assigned
        fields="__all__"

class SubsSerializer(serializers.ModelSerializer):

    class Meta:
        model=Assigned
        fields=['Course']

class ScoreSerializer(serializers.ModelSerializer):

    class Meta:
        model=Score
        fields="__all__"