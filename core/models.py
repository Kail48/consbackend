from django.db import models
import uuid
# Create your models here.
class Country(models.Model):
    name=models.TextField(max_length=50,unique=True)

class Booking(models.Model):
    pid=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    name=models.CharField(max_length=200,blank=True,null=True)
    email=models.EmailField(blank=True,null=True)
    phone=models.CharField(max_length=200,blank=True,null=True)
    country=models.CharField(max_length=200,blank=True,null=True)
    marital_status=models.CharField(max_length=200,blank=True,null=True)
    qualification=models.CharField(max_length=200,blank=True,null=True)
    year_passed=models.CharField(max_length=200,blank=True,null=True)
    course=models.CharField(max_length=200,blank=True,null=True)
    date=models.CharField(max_length=200,blank=True,null=True)
    time=models.CharField(max_length=200,blank=True,null=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Appointment by "+self.name