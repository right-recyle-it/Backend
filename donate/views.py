from django.shortcuts import render
from .models import Donate

# Create your views here.

def index(request):
    donate_list = Donate.objects.all()		# Donate 모델에 있는 정보를 전부 가져온다.
    context = {'donate_list': donate_list}	# donate_list의 정보를 context에 담는다.

    return render(request, 'donate/index.html', context)