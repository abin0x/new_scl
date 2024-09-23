from django.contrib import admin
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'teacher_name', 'rating', 'created_at')  # Include created_at here
    list_filter = ('rating', 'created_at')
    search_fields = ('user', 'course__name', 'teacher_name__username')

      # Order by created_at by default

admin.site.register(Review, ReviewAdmin)