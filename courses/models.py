from django.db import models
from django.conf import settings
from django.utils import timezone
class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    department = models.CharField(max_length=100)
    # image = models.ImageField(upload_to='courses/images/', null=True, blank=True)
    image_url = models.URLField(max_length=500, null=True, blank=True)
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='courses', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

