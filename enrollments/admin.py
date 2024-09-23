from django.contrib import admin
from .models import Enrollment
from users.models import CustomUser  # Make sure to import the CustomUser model

class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'date_enrolled']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "student":
            kwargs["queryset"] = CustomUser.objects.filter(user_type='student')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Enrollment, EnrollmentAdmin)
