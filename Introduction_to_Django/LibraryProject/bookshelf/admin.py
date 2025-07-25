"""from django.contrib import admin
from .models import CustomUser

# Register your models here.
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
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author','publication_year')
    #search_fields = ('title', 'author')
    list_filter = ('publication_year',)
"""

