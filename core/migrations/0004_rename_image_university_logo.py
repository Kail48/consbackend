# Generated by Django 4.1.7 on 2023-05-24 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_story_id_remove_university_id_story_pid_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='university',
            old_name='image',
            new_name='logo',
        ),
    ]