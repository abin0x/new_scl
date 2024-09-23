from rest_framework import serializers
from .models import Course
from users.serializers import UserSerializer

class CourseSerializer(serializers.ModelSerializer):
    teacher = UserSerializer(read_only=True)
    image_url = serializers.CharField(required=False, allow_blank=True) 

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'department', 'image_url', 'teacher', 'created_at', 'updated_at']

    def create(self, validated_data):
        image_url = validated_data.pop('image_url', None)
        course = super().create(validated_data)
        if image_url:
            course.image_url = image_url 
            course.save()
        return course

