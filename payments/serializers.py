# payments/serializers.py
from rest_framework import serializers
from courses.models import Course
from rest_framework import serializers
from .models import Order, Course
from courses.serializers import CourseSerializer

class OrderSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ['id','user', 'course', 'tran_id', 'amount', 'ordered', 'order_date']
