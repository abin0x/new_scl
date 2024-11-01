from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),  
    path('api/', include('courses.urls')), 
    path('api/', include('enrollments.urls')),
    path('api/', include('service.urls')),
    path('api/', include('contact_us.urls')),
    path('api/', include('blog.urls')),
    path('api/', include('reviews.urls')),
    path('api/', include('payments.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

