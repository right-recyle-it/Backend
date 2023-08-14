from django.shortcuts import render, redirect
from .models import Donate

# Create your views here.


def btton(request):
    return render(request, 'map.html')


def index(request):
    if request.method == 'GET':
        return render(request, 'donate/donate.html')
    else:
        name = request.POST.get('name')
        kind = request.POST.get('kind')
        condition = request.POST.get('condition')
        upgrade = request.POST.get('upgrade')
        last_update = request.POST.get('last_update')
        Donate.objects.create(
            name=name,
            kind=kind,
            condition=condition,
            upgrade=upgrade,
            last_update=last_update
        )
        return render(request, 'map.html')
