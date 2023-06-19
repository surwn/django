from django.db import models
from django.utils.translation import ugettext_lazy as _

class Hotel(models.Model):
    name = models.CharField(_("Name"), max_length=255)
    address = models.CharField(_("Address"), max_length=255)
    description = models.TextField(_("Description"))

    def __str__(self):
        return self.name

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_number = models.CharField(_("Room number"), max_length=50)
    price = models.DecimalField(_("Price"), max_digits=10, decimal_places=2)
    description = models.TextField(_("Description"))

    def __str__(self):
        return "{} - {}".format(self.hotel.name, self.room_number)

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    guest_name = models.CharField(_("Guest name"), max_length=255)
    check_in_date = models.DateField(_("Check-in date"))
    check_out_date = models.DateField(_("Check-out date"))
    total_price = models.DecimalField(_("Total price"), max_digits=10, decimal_places=2)

    def __str__(self):
        return "{} - {} ({})".format(self.guest_name, self.room.hotel.name, self.room.room_number)

