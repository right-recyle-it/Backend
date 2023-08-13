from django.contrib import admin
from .models import Get
# Register your models here.

class GetAdmin(admin.ModelAdmin):
    search_fields = ['get']

admin.site.register(Get, GetAdmin)