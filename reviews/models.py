from django.db import models
from django.conf import settings
from courses.models import Course  # Assuming you have a Course model
from django.utils import timezone
STAR_CHOICES = [
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
]

class Review(models.Model):
    user = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.CharField(max_length=5, choices=STAR_CHOICES)
    comment = models.TextField()
    # image = models.ImageField(upload_to='review_images/', blank=True, null=True)
    image = models.URLField(max_length=500, null=True, blank=True)
    # profile_image = models.URLField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField( auto_now_add=True)

    def __str__(self):
        return f'Review by {self.user} for {self.course}'