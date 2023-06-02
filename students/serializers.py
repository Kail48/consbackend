from rest_framework import serializers
from .models import StudentProfile,DocumentCategory,DocumentFile
from django.contrib.auth import get_user_model
User=get_user_model()

class DocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model=DocumentFile
        fields='__all__'

class DocumentCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model=DocumentCategory
        fields='__all__'
   


class DocumentListSerializer(serializers.ModelSerializer):
    file_link=serializers.SerializerMethodField()
    class Meta:
        model=DocumentFile
        fields=['id','filename','category','created','file_link','verified','verified_by','feedback','feedback_by']
    def get_file_link(self,obj):
        request = self.context.get('request')
        if bool(obj.file):
            return str(request.build_absolute_uri(obj.file.url))
        else:
            return None
    
class StudentProfileListSerializer(serializers.ModelSerializer):

    profile_pic=serializers.SerializerMethodField()
    class Meta:
        model=StudentProfile
        fields=['id','name','checked','country','phone','address','profile_pic']
    def get_profile_pic(self,obj):
        request = self.context.get('request')
        if bool(obj.profile_picture):
            return str(request.build_absolute_uri(obj.profile_picture.url))
        else:
            return None
    
class StudentProfileSerializer(serializers.ModelSerializer):
    profile_pic=serializers.SerializerMethodField()
    class Meta:
        model=StudentProfile
        fields=['id','name','checked','country','phone','address','profile_pic']
    def get_profile_pic(self,obj):
        request = self.context.get('request')
        if bool(obj.profile_picture):
            return str(request.build_absolute_uri(obj.profile_picture.url))
        else:
            return None

