from django.shortcuts import render, redirect
from .models import Get

# Create your views here.


def main(request):
    return render(request, 'frontend/html/mainpage.html')


def index(request):
    if request.method == 'GET':
        return render(request, 'frontend/html/기기받기.html')
    else:
        name = request.POST.get('name')
        kind = request.POST.get('kind')
        address = request.POST.get('address')
        reason = request.POST.get('reason')
        last_update = request.POST.get('last_update')
        Get.objects.create(
            name=name,
            kind=kind,
            address=address,
            reason=reason,
            last_update=last_update
        )
        return redirect('/')
