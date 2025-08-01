# Generated by Django 5.2.4 on 2025-07-27 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0003_book'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Editor',
            new_name='UserActivity',
        ),
        migrations.AlterModelOptions(
            name='useractivity',
            options={'ordering': ['name'], 'permissions': [('can_vew', 'can_create'), ('can_edit', 'can_delete')], 'verbose_name': 'user activity', 'verbose_name_plural': 'activities'},
        ),
    ]
