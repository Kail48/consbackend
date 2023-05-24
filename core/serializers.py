from rest_framework import serializers
from .models import Country,Booking,University,Story
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
User=get_user_model()

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model= Country
        fields='__all__'

class RegisterStaffSerializer(serializers.ModelSerializer):
    password1=serializers.CharField(style={'input_type':'password'},write_only=True,required=True)
    password2=serializers.CharField(style={'input_type':'password'},write_only=True,required=True)

    class Meta:
        model=User
        fields=[
            'username',
            'first_name',
            'last_name',
            'password1',
            'password2'
        ]
        extra_kwargs={
            'first_name':{'required':True},
            'last_name':{'required':True},
        }
    def create(self,validated_data):
        username=validated_data.get('username')
        firstName=validated_data.get('first_name')
        lastName=validated_data.get('last_name')
        password1=validated_data.get('password1')
        password2=validated_data.get('password2')
        if password1!=password2:
            raise serializers.ValidationError({'password':'passwords must match'})
        user=User(username=username,first_name=firstName,last_name=lastName,is_staff=True)
        user.set_password(password1)
        user.save()
        return user
    
class RegisterStudentSerializer(serializers.ModelSerializer):
    password1=serializers.CharField(style={'input_type':'password'},write_only=True,required=True)
    password2=serializers.CharField(style={'input_type':'password'},write_only=True,required=True)
    email=serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    class Meta:
        model=User
        fields=[
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]
        extra_kwargs={
            'first_name':{'required':True},
            'last_name':{'required':True},
        }
    def create(self,validated_data):
        username=validated_data.get('username')
        firstName=validated_data.get('first_name')
        lastName=validated_data.get('last_name')
        password1=validated_data.get('password1')
        password2=validated_data.get('password2')
        email=validated_data.get('email')
        if password1!=password2:
            raise serializers.ValidationError({'password':'passwords must match'})
        user=User(username=username,first_name=firstName,last_name=lastName,email=email)
        user.set_password(password1)
        user.save()
        return user
    
class StudentUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=User
        fields=['id','username','first_name','last_name','email']

class StaffUserSerializer(serializers.ModelSerializer):
   
    class Meta:
        model=User
        fields=['id','username','first_name','last_name']

class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model=Booking
        fields=['pid','name','email','phone','country','marital_status','qualification','year_passed','course','date','time']

class UniversitySerializer(serializers.ModelSerializer):

    class Meta:
        model=University
        fields=["name","link","logo"]



class StorySerializer(serializers.ModelSerializer):
    img=serializers.SerializerMethodField()
    class Meta:
        model=Story
        fields=["name","country","image","text",'img']
    def get_img(self,obj):
        request = self.context.get('request')
        return str(request.build_absolute_uri(obj.image.url))

