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
    return render(request,'index.html')