from django.contrib import admin
from .models import Destination

class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name', 'travel_type', 'source', 'destination', 'datetime', 'price', 'available_seats')
    list_filter = ('travel_type', 'source', 'destination')
    search_fields = ('name', 'description')

admin.site.register(Destination, DestinationAdmin)
