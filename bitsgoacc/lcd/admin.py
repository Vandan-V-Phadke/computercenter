from django.contrib import admin
from .models import *


@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    #list_display = ('description', 'image')
    pass
