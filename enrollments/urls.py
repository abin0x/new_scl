# enrollments/urls.py
from django.urls import path
from .views import EnrollCourseAPIView, EnrollmentHistoryAPIView

urlpatterns = [
    path('enroll/', EnrollCourseAPIView.as_view(), name='enroll-course'),
    path('history/', EnrollmentHistoryAPIView.as_view(), name='enrollment-history'),
]
