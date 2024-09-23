# enrollments/serializers.py
from rest_framework import serializers
from .models import Enrollment
from courses.models import Course
from courses.serializers import CourseSerializer
from users.models import CustomUser

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'profile_image']


class EnrollmentSerializer(serializers.ModelSerializer):
    course = CourseSerializer()
    student = StudentSerializer()

    class Meta:
        model = Enrollment
        fields = ['student', 'course', 'date_enrolled']

class EnrollCourseSerializer(serializers.ModelSerializer):
    course_id = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(),
        source='course'  # Maps `course_id` to the `course` field in the model
    )

    class Meta:
        model = Enrollment
        fields = ['course_id']
