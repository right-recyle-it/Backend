from django.contrib import admin
from .models import Donate

# Register your models here.

class DonateAdmin(admin.ModelAdmin):
    search_fields = ['kind']

admin.site.register(Donate, DonateAdmin)


