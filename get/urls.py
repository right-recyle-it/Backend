from django.urls import path

from .views import index,main

app_name = 'get'
urlpatterns = [
    # path('', main, name='main'),
    path('', index, name='get'),
]