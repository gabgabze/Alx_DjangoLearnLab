from django.contrib import admin
from .models import Editor

class EditorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

admin.site.register(Editor, EditorAdmin)