from django.db import models
from advanced_features_and_security.LibraryProject.LibraryProject.settings import AUTH_USER_MODEL


class Editor(models.Model):
    name = models.CharField(max_length=100)
    profile = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Editor'
        verbose_name_plural = 'Editors'
        ordering = ['name']
        permissions = [('can_vew','can_create','can_edit', 'can_delete')]