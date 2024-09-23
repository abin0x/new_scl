from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, PostDetail

router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('posts/<int:pk>', PostDetail.as_view(), name='post-detail'), 
]
