from django.shortcuts import render
from .models import Get

# Create your views here.

def index(request):
    get_list = Get.objects.all()		# Get 모델에 있는 정보를 전부 가져온다.
    context = {'get_list': get_list}	# get_list의 정보를 context에 담는다.

    return render(request, 'get/index.html', context)