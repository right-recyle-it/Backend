"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from map.views import map_view, main, education, mypage, mydevice, template, device_instructions, myinformation
from get.views import main
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import routers
from user.views import KakaoLoginView
# from pybo import views
# from user.views import kakakoView
router = routers.DefaultRouter()  # DefaultRouter를 설정
# router.register('Item', views.ItemViewSet) #itemviewset 과 item이라는 router 등록

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0),
         name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),

    path('admin/', admin.site.urls),
    path('', main),
    path('map/', map_view, name='map'),
    # path('accounts/', include('accounts.urls', namespace='accounts')),
    path('donate/', include('donate.urls', namespace='donate')),
    path('get/', include('get.urls', namespace='get')),
    path('kakao/login/', KakaoLoginView.as_view()),
    # path('kakao/login/callback/', KakaoCallbackView.as_view()),
    # path('oauth/kakao/login/callback', KakaoCallbackView.as_view()),
    path('common/', include('common.urls')),

    path('education/', education),
    path('education/template/', template),
    path('education/deviceinstruction/', device_instructions),

    path('mypage/', mypage),
    path('mypage/mydevice/', mydevice),
    path('mypage/myinformation/', myinformation),
    # path('', views.index, name='index'),  # '/' 에 해당되는 path
]
