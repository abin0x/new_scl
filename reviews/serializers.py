from rest_framework import serializers
from .models import Review
from courses.models import Course 
from django.contrib.auth import get_user_model

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title']  

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username'] 

class ReviewSerializer(serializers.ModelSerializer):
    course = CourseSerializer()
    teacher_name = UserSerializer()

    class Meta:
        model = Review
        fields = ['id', 'user', 'course', 'teacher_name', 'rating', 'comment', 'image', 'created_at']
