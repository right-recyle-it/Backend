from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Location
from get.models import Get
from donate.models import Donate
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


@login_required
def education(request):
    return render(request, 'frontend/html/information-sharing.html')

@login_required
def mypage(request):
    return render(request, 'frontend/html/마이페이지.html')

def mydevice(request):
    get = Get.objects.all()
    donate = Donate.objects.all()
    context = {
        'get_list' : get,
        'donate_list' : donate,
    }
    return render(request, 'frontend/html/my_device.html', context)

def myinformation(request):
    return render(request, 'frontend/html/my_information.html')

def template(request):
    return render(request, 'frontend/html/free-template-download.html')

def device_instructions(request):
    return render(request, 'frontend/html/device-instructions.html')


