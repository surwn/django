import stripe
from django.conf import settings
from .models import Booking

stripe.api_key = settings.STRIPE_SECRET_KEY

def process_payment(request, booking_id):
    booking = Booking.objects.get(pk=booking_id)

    try:
        charge = stripe.Charge.create(
            amount=int(booking.total_price * 100),
            currency='usd',
            description='Hotel booking',
            source=request.POST['stripeToken']
        )
        booking.payment_id = charge.id
        booking.save()
        return True
    except stripe.error.CardError as e:
        return False, e.json_body['error']['message']

