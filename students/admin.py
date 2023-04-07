from django.contrib import admin
from .models import StudentProfile,DocumentCategory,DocumentFile
# Register your models here.
admin.site.register(StudentProfile)
admin.site.register(DocumentFile)
admin.site.register(DocumentCategory)