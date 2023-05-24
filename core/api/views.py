from rest_framework.response import Response
from rest_framework.decorators import api_view
from core.models import Country,Booking
from core.serializers import CountrySerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from core.permissions import IsSuperUser
from django.contrib.auth import get_user_model
from rest_framework import status
from students.models import StudentProfile
from core.serializers import RegisterStaffSerializer,RegisterStudentSerializer,StudentUserSerializer,StaffUserSerializer,BookingSerializer

User=get_user_model()

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['isStaff']=user.is_staff
        token['isAdmin']=user.is_superuser
        return token
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class=MyTokenObtainPairSerializer

@api_view(['GET'])
def welcome(request):
    data={'message':"Hello"}
    return Response(data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def testAuth(request):
    return Response({'name':request.user.username,'isStaff':request.user.is_staff,'isAdmin?':request.user.is_superuser})


@api_view(['GET'])
@permission_classes([IsSuperUser])
def testAuthAdmin(request):
    return Response({'message':'hello '+request.user.username})

@api_view(['POST'])
@permission_classes([IsSuperUser])
def createStaffUser(request):
    serializer=RegisterStaffSerializer(data=request.data)
    data={}
    if serializer.is_valid():
        user=serializer.save()
        data['response']='successfully created a new staff user'
        data['username']=user.username
    else:
        data=serializer.errors
    return Response(data,status=status.HTTP_400_BAD_REQUEST)

from django.conf import settings
@api_view(['POST'])
@permission_classes([IsAdminUser])
def createStudentUser(request):
    serializer=RegisterStudentSerializer(data=request.data)
    password=request.data.get('password1')
    data={}
    if serializer.is_valid():
        user=serializer.save()
        profile=StudentProfile.objects.create(student=user,name=user.first_name+" "+user.last_name)
        profile.save()
        subject="Registration at Details Education"
        message=f"\t\t WELCOME TO DETAIL EDUCATION \n\n\n\n\nHello,{user.first_name},\nYour new account has been created at the Details education website with the following credentials:\nUsername:{user.username}\nPassword:{password}\nWelcome Aboard, Use the details website to benefit from different feature that will only make things more convinient for you.\n\n\n\n\nNote:PLEASE CHANGE YOUR PASSWORD AFTER THE FIRST LOGIN."
        try:
            user.email_user(subject,message,settings.EMAIL_HOST_USER)
        except:
            user.delete()
            return Response({'message':"Email sevice not working"},status=status.HTTP_400_BAD_REQUEST)
        data['response']='successfully created a new student user'
        data['username']=user.username
    else:
        data=serializer.errors
    return Response(data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def getStudents(request):
    students=User.objects.filter(is_superuser=False,is_staff=False)
    print(students)
    serializer=StudentUserSerializer(students,many=True)
    return Response(serializer.data)

@api_view(['DELETE','GET'])
@permission_classes([IsAdminUser])
def deleteStudent(request):
    if request.data.get('id'):
        if request.method=='DELETE':
            try:
                student=User.objects.get(id=request.data.get('id'))
                data={'message':'Successfully deleted student user with username '+student.username}
                student.delete()
                return Response(data)
            except:
                data={'message':'ID does not match any student in the database'}
                return Response(data,status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                student=User.objects.get(id=request.data.get('id'))
                serializer=StudentUserSerializer(student)
                return Response(serializer.data)
            except:
                 data={'message':'ID does not match any student in the database'}
                 return Response(data,status=status.HTTP_400_BAD_REQUEST)
#send request in the body

@api_view(['GET'])
@permission_classes([IsSuperUser])
def getStaffs(request):
    staffs=User.objects.filter(is_superuser=False,is_staff=True)
    print(staffs)
    serializer=StaffUserSerializer(staffs,many=True)
    return Response(serializer.data)

@api_view(['DELETE','GET'])
@permission_classes([IsSuperUser])
def deleteStaff(request):
    if request.data.get('id'):
        if request.method=='DELETE':
            try:
                staff=User.objects.get(id=request.data.get('id'))
                data={'message':'Successfully deleted staff user with username '+staff.username}
                staff.delete()
                return Response(data)
            except:
                data={'message':'ID does not match any staff in the database'}
                return Response(data,status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                staff=User.objects.get(id=request.data.get('id'))
                serializer=StaffUserSerializer(staff)
                return Response(serializer.data)
            except:
                 data={'message':'ID does not match any staff in the database'}
                 return Response(data,status=status.HTTP_400_BAD_REQUEST)
            
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def changePassword(request):
    if request.data:
        old_password=request.data.get("old_password")
        password=request.data.get("password")
        password2=request.data.get("password2")
        if password!=password2:
            return Response({'password':'The two passwords must match'},status=status.HTTP_400_BAD_REQUEST)
        else:
            user=request.user
            if user.check_password(old_password):
                if old_password==password:
                    return Response({'password':'New password cannot be old password'},status=status.HTTP_400_BAD_REQUEST)
                user.set_password(password)
                user.save()
                
                return Response({"message":"Successfully changed user password"})
            else:
                return Response({"message":"Old password does not match"},status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST','DELETE'])
@permission_classes([IsAdminUser])
def bookingView(request):
   
    if request.method=='GET':
        bookings=Booking.objects.all()
        serializer=BookingSerializer(bookings,many=True)
        return Response(serializer.data)
    if request.method=='DELETE':
        if request.data.get('pid'):
            try:
                booking=Booking.objects.get(pid=request.data.get('pid'))
                booking.delete()
                return Response({"message":"Successfully deleted booking"})
            except:
                return Response({"message":"No such Booking in the database"},status=status.HTTP_400_BAD_REQUEST)
            
@api_view(['POST'])
def createBooking(request):
     if request.method=='POST':
        serializer=BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Successfully booked"})
        else:
            return Response({"message":"The data is not correct"},status=status.HTTP_400_BAD_REQUEST)