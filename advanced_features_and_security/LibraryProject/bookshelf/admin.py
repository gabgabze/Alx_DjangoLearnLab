from django.contrib import admin
from .models import CustomUser,UserActivity

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = ['email','date_of_birth','profile_photo']
# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserActivity)


