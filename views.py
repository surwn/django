from django.views.generic.list import ListView
from .models import Hotel

class HotelSearchView(ListView):
    model = Hotel
    template_name = 'hotel_search.html'

    def get_queryset(self):
        qs = super().get_queryset()
        city = self.request.GET.get('city')

        if city:
            qs = qs.filter(address__icontains=city)

        return qs
