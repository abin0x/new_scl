from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=50)
    # image = models.ImageField(upload_to='blog_images/', blank=True, null=True) 
    image = models.URLField(max_length=500, null=True, blank=True) 
    # image_url = models.URLField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Created date

    def __str__(self):
        return self.title
