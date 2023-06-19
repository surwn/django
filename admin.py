from django.contrib import admin
from .models import Hotel, Room, Booking

class RoomInline(admin.TabularInline):
    model = Room

class HotelAdmin(admin.ModelAdmin):
    inlines = [RoomInline]

admin.site.register(Hotel, HotelAdmin)
admin.site.register(Room)
admin.site.register(Booking)