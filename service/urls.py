# service/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServiceViewset

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'services', ServiceViewset, basename='service')

urlpatterns = [
    path('', include(router.urls)),  # Include the router URLs
]
