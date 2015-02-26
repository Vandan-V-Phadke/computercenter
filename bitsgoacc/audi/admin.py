from django.contrib import admin
from .models import BookingRequest


class BookingRequestAdmin(admin.ModelAdmin):
    pass

admin.site.register(BookingRequest, BookingRequestAdmin)
