from django.urls import path

from .views import index, button

urlpatterns = [
    path('', button),
    path('donatee', index),
]
