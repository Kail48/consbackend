from django.db import models
from django.contrib.auth import get_user_model
import uuid
# Create your models here.
User=get_user_model()
class StudentProfile(models.Model):
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    name=models.CharField(max_length=200,null=True)
    student=models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=200,null=True)
    country=models.CharField(max_length=200,null=True)
    profile_picture=models.ImageField(null=True,blank=True,upload_to='images/')
    checked=models.BooleanField(default=False)
    joined_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student.username+" profile"
    def checkProfile(self):
        self.checked=True

class DocumentCategory(models.Model):
    name=models.CharField(max_length=200,unique=True,primary_key=True)

    def __str__(self):
        return self.name

class DocumentFile(models.Model):
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    owner=models.ForeignKey(StudentProfile,on_delete=models.CASCADE)
    category=models.ForeignKey(DocumentCategory,on_delete=models.CASCADE,null=True)
    created=models.DateTimeField(auto_now_add=True)
    filename=models.CharField(max_length=200,null=True)
    file=models.FileField(blank=False,null=True,upload_to='others/')
    verified=models.BooleanField(default=False)
    verified_by=models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.filename
    
    def set_owner(self,user,type):
        self.owner=user
        self.category=type
        self.save()

    def verify(self,staff_name):
        self.verified=True
        self.verified_by=staff_name
        self.save()
    

