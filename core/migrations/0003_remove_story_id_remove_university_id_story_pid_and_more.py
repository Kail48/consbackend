# Generated by Django 4.1.7 on 2023-05-23 17:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_story_university'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='id',
        ),
        migrations.RemoveField(
            model_name='university',
            name='id',
        ),
        migrations.AddField(
            model_name='story',
            name='pid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AddField(
            model_name='university',
            name='pid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
