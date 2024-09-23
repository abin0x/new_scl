from django.db import models

# Create your models here.
class Service(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    # image=models.ImageField(upload_to="service/images/")
    image = models.URLField(max_length=500, null=True, blank=True)
    
    def __str__(self):
        return self.name