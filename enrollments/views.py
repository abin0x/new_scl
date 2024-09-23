# enrollments/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Enrollment
from .serializers import EnrollmentSerializer, EnrollCourseSerializer
from rest_framework.permissions import IsAuthenticated

class EnrollCourseAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = EnrollCourseSerializer(data=request.data)
        if serializer.is_valid():
            course = serializer.validated_data['course']
            student = request.user
            if Enrollment.objects.filter(student=student, course=course).exists():
                return Response({"error": "Already enrolled in this course."}, status=status.HTTP_400_BAD_REQUEST)
            
            enrollment = Enrollment(student=student, course=course)
            enrollment.save()
            return Response({"detail": "Enrolled successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EnrollmentHistoryAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        student = request.user
        enrollments = Enrollment.objects.filter(student=student)
        serializer = EnrollmentSerializer(enrollments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
