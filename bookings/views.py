# bookings/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Booking
from travel_options.models import Destination

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-booking_date')
    return render(request, 'bookings/my_bookings.html', {'bookings': bookings})

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if booking.status != 'canceled':
        booking.status = 'canceled'
        booking.save()

        # Return seats back to destination
        booking.destination.available_seats += booking.seats
        booking.destination.save()

        messages.success(request, f'Booking for {booking.destination.name} has been canceled.')

    return redirect('my_bookings')