from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # Specify the fields to be displayed in the list view
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'user_type', 'is_staff', 'is_active'
    )
    
    # Specify the fields to be used for filtering the list view
    list_filter = ('user_type', 'is_staff', 'is_active')

    # Define the fields to be used in the detail view
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'profile_image')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('User Type', {'fields': ('user_type',)}),
    )

    # Define the fields to be included in the form for adding and changing users
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'user_type'),
        }),
    )

    # Define the ordering of the list view
    ordering = ('username',)
    
    # Specify the fields to be included in search
    search_fields = ('username', 'email', 'first_name', 'last_name')

# Register the CustomUser model with the CustomUserAdmin class
admin.site.register(CustomUser, CustomUserAdmin)
