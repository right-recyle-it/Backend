from django.shortcuts import render, redirect
from .models import Donate

# Create your views here.


def button(request):
    return render(request, 'map.html')


def index(request):
    if request.method == 'GET':
        return render(request, 'donate/donate.html')
    else:
        # donate_list = Donate.objects.all()		# Donate 모델에 있는 정보를 전부 가져온다.
        # context = {'donate_list': donate_list}	# donate_list의 정보를 context에 담는다.
        name = request.POST.get('name')
        # kind = request.POST.get('kind')
        # condition = request.POST.get('condition')
        # upgrade = request.POST.get('upgrade')
        Donate.objects.create(
            name=name
            # kind=kind,
            # condition=condition,
            # upgrade=upgrade
        )
        return redirect('button')

    # @login_required
# def post_create(request):
#     if request.method == 'GET':
#         return render(request, 'instagram/post_form.html')
#     else:
#         image = request.FILES.get('image')
#         content = request.POST.get('content')
#         Post.objects.create(
#             image = image,
#             content = content,
#             writer = request.user
#         )
#         return redirect('index')
