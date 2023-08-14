from django.urls import path

from .views import index, btton
app_name = 'donate'

urlpatterns = [
    path('', btton),
    path('donatee', index),
]
