from django.urls import path

from .views import index
app_name = 'donate'

urlpatterns = [
    path('', index, name='donate'),
]
