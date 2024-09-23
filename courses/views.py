from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Course
from .serializers import CourseSerializer
from .permissions import IsTeacherOrReadOnly

class CourseList(APIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsTeacherOrReadOnly]
    permission_classes = [IsTeacherOrReadOnly]

    def get(self, request, format=None):
        is_teacher_dashboard = request.query_params.get('dashboard') == 'true'
        department = request.query_params.get('department')

        if is_teacher_dashboard and request.user.is_authenticated:
            courses = Course.objects.filter(teacher=request.user)
        else:
            courses = Course.objects.all()
        # 1 no problem 
        if department:
            courses = courses.filter(department=department)

        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(teacher=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    


class CourseDetail(APIView):
    permission_classes = [permissions.IsAuthenticated, IsTeacherOrReadOnly]
    permission_classes = [IsTeacherOrReadOnly]

    def get_object(self, pk, user):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            raise NotFound(detail="Course not found.")

    def get(self, request, pk, format=None):
        course = self.get_object(pk, request.user)
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        course = self.get_object(pk, request.user)

        if course.teacher != request.user:
            return Response({'detail': 'You do not have permission to edit this course.'}, status=status.HTTP_403_FORBIDDEN)

        serializer = CourseSerializer(course, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        course = self.get_object(pk, request.user)

        if course.teacher != request.user:
            return Response({'detail': 'You do not have permission to delete this course.'}, status=status.HTTP_403_FORBIDDEN)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
