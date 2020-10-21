from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from quickstart.serializers import UserSerializer, GroupSerializer

from django.shortcuts import render
import requests

from rest_framework.renderers import JSONRenderer, StaticHTMLRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.decorators import api_view, renderer_classes
from zeep import Client


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ProfileList(APIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
        geodata = response.json()
       
        data = {
            'userid': geodata['userId'],
            'id': geodata['id'],
            'title': geodata['title'],
            'completed': geodata['completed']
        }
        return render(request, 'home.html', data)


class WeatherList(APIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        response = requests.get('https://api.openweathermap.org/data/2.5/weather?q=London&appid=754e02b29f381b8608ff3d9109f5bcb5')
        weatherdata = response.json()
       
        data = {
            'coord': weatherdata['coord'],
            'weather': weatherdata['weather'],
            'base': weatherdata['base'],
            'visibility': weatherdata['visibility']
        }
        return render(request, 'weather.html', data)


def simple_html_view(request):
    response = requests.get('http://freegeoip.net/json/')
    geodata = response.json()
    return render(request, 'core/home.html', {
        'ip': geodata['ip'],
        'country': geodata['country_name']
    })


@api_view(['GET'])
@renderer_classes([TemplateHTMLRenderer])
def home(request):

    client = Client('http://www.dneonline.com/calculator.asmx?WSDL')
    result = client.service.Subtract(
        200, 200)

    print(f"The result is {result}")

    return render(request, 'soap.html', {
       
    })


@api_view(['GET'])
@renderer_classes([StaticHTMLRenderer])
def deck(request):
    renderer_classes = [TemplateHTMLRenderer]
    data = '<html><body><h1>Hello, world</h1></body></html>'

    client = Client('http://www.dneonline.com/calculator.asmx?WSDL')
    result = client.service.Add(
        200, 200)

    print(result)

    # http://www.dneonline.com/calculator.asmx?
    return Response(data)

    

