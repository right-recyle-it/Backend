from django.shortcuts import render

from .models import Location
from config import settings

# def map_view(request):
#     locations = Location.objects.all()
#     #return render(request, 'map.html', {'locations': locations})
#     return render(request, 'kakakomap.html', {'locations': locations})
from django.core.serializers import serialize
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def map_view(request):
    locations = Location.objects.all()
    context = {
        'locations': serialize('json', locations),
        'api_key': settings.KAKAO_MAPS_API_KEY,
    }
    return render(request, 'kakakomap.html', context)


def main(request):
    return render(request, 'frontend/html/mainpage.html')


def education(request):
    return render(request, 'frontend/html/information-sharing.html')


def mypage(request):
    return render(request, 'frontend/html/마이페이지.html')


def mydevice(request):
    return render(request, 'frontend/html/my_device.html')

def myinformation(request):
    return render(request, 'frontend/html/my_information.html')

def template(request):
    return render(request, 'frontend/html/free-template-download.html')

def device_instructions(request):
    return render(request, 'frontend/html/device-instructions.html')


