from rest_framework import serializers
from .models import StudentProfile,DocumentCategory,DocumentFile
from django.contrib.auth import get_user_model
User=get_user_model()

class DocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model=DocumentFile
        fields='__all__'

class DocumentListSerializer(serializers.ModelSerializer):

    class Meta:
        model=DocumentFile
        fields=['id','filename','category','created','file']

class StudentProfileListSerializer(serializers.ModelSerializer):

    class Meta:
        model=StudentProfile
        fields=['id','name','profile_picture','checked']
        

