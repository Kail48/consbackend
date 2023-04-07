from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import StudentProfile,DocumentCategory,DocumentFile
from .serializers import DocumentSerializer,DocumentListSerializer,StudentProfileListSerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from core.permissions import IsSuperUser
from rest_framework import status
from django.contrib.auth import get_user_model
User=get_user_model()
# Create your views here.
@permission_classes([IsAuthenticated])
@api_view(['POST','GET'])
def getuploadDocument(request):
    if request.method=='POST':
        if request.data.get('filename'):
            filename=request.data.get('filename')
        else:
            filename=''
        if request.data.get('category'):
            category=DocumentCategory.objects.get(name=request.data.get('category'))
        else:
            return Response({"message":"Document category must be provided"},status=status.HTTP_400_BAD_REQUEST)
        if request.FILES.get('file'):
            file=request.FILES.get('file')
        else:
            return Response({"message":"file must be present"},status=status.HTTP_400_BAD_REQUEST)
        user=request.user
        profile=None
        try:
            
            profile=StudentProfile.objects.get(student=user)
            
        except:
            pass
        if profile is not None:
            document=DocumentFile.objects.create(filename=filename,owner=profile,file=file,category=category)
            document.save()
            return Response({"message":"successfully created document for"+str(user)}) 
        else:
            return Response({"message":"Only registered users can upload documents."},status=status.HTTP_400_BAD_REQUEST)
    if request.method=='GET':
        pass

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getDocuments(request):
    profile=None
    try:
        profile=StudentProfile.objects.get(student=request.user)
    except:
        pass
    if profile is not None:
        documents=DocumentFile.objects.filter(owner=profile)
        serializer=DocumentListSerializer(documents,many=True)
        return Response(serializer.data) 
    else:
        return Response({"message":"Only registered users can upload documents."},status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@permission_classes([IsAdminUser])
def getStudentProfiles(request):
    profiles=StudentProfile.objects.all()
    serializer=StudentProfileListSerializer(profiles,many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def getStudentDocuments(request):
    if request.data.get('id'):
        id=request.data.get('id')
        profile=StudentProfile.objects.get(id=id)
        if profile is None:
            return Response({"message":"Student does not exist"},status=status.HTTP_400_BAD_REQUEST)
        documents=DocumentFile.objects.filter(owner=profile)
        serializer=DocumentListSerializer(documents,many=True)
        return Response(serializer.data)
    else:
        return Response({"message":"Student id not specified"},status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
@permission_classes([IsAdminUser])
def verifyDocument(request):
    staff=request.user
    name=staff.first_name+" "+staff.last_name
    if request.data.get('id'):
        id=request.data.get('id')
        document=DocumentFile.objects.get(id=id)
        if document is None:
            return Response({"message":"document does not exist"},status=status.HTTP_400_BAD_REQUEST)
        document.verify(name)
        return Response({"message":"Verified document"})
    else:
        return Response({"message":"document id not specified"},status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@permission_classes([IsAdminUser])
def getTotalUsers(request):
    students=StudentProfile.objects.all().count()
    staffs=User.objects.filter(is_staff=True,is_superuser=False).count()
    data={
        "students":students,
        "staffs":staffs
    }
    return Response(data)
        

        
