from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Room, Booking

class RoomBookingForm(forms.Form):
    check_in_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label=_("Check-in date"))
    check_out_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label=_("Check-out date"))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['room'] = forms.ModelChoiceField(queryset=Room.objects.filter(booking__isnull=True), label=_("Room"))

    def clean(self):
        cleaned_data = super().clean()
        check_in_date = cleaned_data.get("check_in_date")
        check_out_date = cleaned_data.get("check_out_date")
        room = cleaned_data.get("room")

        if check_in_date and check_out_date and room:
            if Booking.objects.filter(room=room, check_in_date__lte=check_out_date, check_out_date__gte=check_in_date).exists():
                raise forms.ValidationError(_("This room is already booked for the selected dates."))
