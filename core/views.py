from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Country,University,Story
from .serializers import CountrySerializer,UniversitySerializer,StorySerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework import status
# Create your views here.
@api_view(['GET'])
def test(request):
    countries=Country.objects.all()
    serializer=CountrySerializer(countries,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addTest(request):
    serializer=CountrySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['GET'])
def getTest(request,name):
    country=Country.objects.get(name=name)
    if country is not None:
        return Response(CountrySerializer(country).data)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def addUniversity(request):
    name=None
    link=''
    image=None
    if request.data.get('name'):
        name=request.data.get('name')
    if request.data.get('link'):
        link=request.data.get('link')
    if request.FILES.get('image'):
        image=request.FILES.get('image')
    if name is not None and image is not None:
        uni=University.objects.create(name=name,link=link,image=image)
        uni.save()
        return Response({'message':'saved successfully'})
    else:
        return Response({'message':'please provide valid data'},status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
@permission_classes([IsAdminUser])
def addStory(request):
    name=None
    country=None
    image=None
    text=None
    if request.data.get('name'):
        name=request.data.get('name')
    if request.data.get('country'):
        country=request.data.get('country')
    if request.data.get('text'):
        text=request.data.get('text')
    if request.FILES.get('image'):
        image=request.FILES.get('image')
    if name is not None and image is not None and country is not None:
        story=Story.objects.create(name=name,country=country,image=image,text=text)
        story.save()
        return Response({'message':'saved successfully'})
    else:
        return Response({'message':'please provide valid data'},status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['Get'])
def getUniversities(request):
    universities=University.objects.all()
    if universities is not None:
        return Response(UniversitySerializer(universities,many=True,context={'request':request}).data)

@api_view(['Get'])
def getStories(request):
    stories=Story.objects.all()
    if stories is not None:
        return Response(StorySerializer(stories,many=True,context={'request':request}).data)



 