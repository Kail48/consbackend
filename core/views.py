from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Country
from .serializers import CountrySerializer
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