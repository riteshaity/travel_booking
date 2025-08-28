from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'destination', 'booking_date', 'status')
    search_fields = ('user__username', 'destination__name')
    list_filter = ('status', 'booking_date')
