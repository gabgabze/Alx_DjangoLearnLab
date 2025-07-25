from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = ['email','date_of_birth','profile_photo']
    fieldsets = [
        ('Title', {
            'fields': [
                '', 
            ],
        }),
    ]
# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)