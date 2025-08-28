# travel_options/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime

from .models import Destination
from bookings.models import Booking


def destinations_list(request):
    """
    List all destinations with optional filters.
    """
    travel_type = request.GET.get('type')
    source = request.GET.get('source')
    destination_name = request.GET.get('destination')
    date = request.GET.get('date')

    travels = Destination.objects.all()

    if travel_type:
        travels = travels.filter(travel_type__iexact=travel_type)
    if source:
        travels = travels.filter(source__icontains=source)
    if destination_name:
        travels = travels.filter(destination__icontains=destination_name)
    if date:
        try:
            travel_date = datetime.strptime(date, "%Y-%m-%d").date()
            travels = travels.filter(datetime__date=travel_date)
        except ValueError:
            pass

    context = {
        'travels': travels,
        'filters': {
            'type': travel_type or '',
            'source': source or '',
            'destination': destination_name or '',
            'date': date or '',
        }
    }
    return render(request, 'travel_options/destinations_list.html', context)


@login_required
def destination_detail(request, destination_id):
    """
    Show details for a single destination and handle booking form submission.
    """
    travel = get_object_or_404(Destination, id=destination_id)

    if request.method == 'POST':
        seats_requested = int(request.POST.get('seats', 1))

        if seats_requested > travel.available_seats:
            messages.error(request, f"Only {travel.available_seats} seats available!")
            return redirect('destination_detail', destination_id=destination_id)

        # Deduct seats and save
        travel.available_seats -= seats_requested
        travel.save()

        # Create booking
        total_price = seats_requested * travel.price
        Booking.objects.create(
            user=request.user,
            destination=travel,
            seats=seats_requested,
            total_price=total_price,
            status='confirmed'
        )

        messages.success(request, f"Booking confirmed for {travel.name}! Total: ₹{total_price}")
        return redirect('my_bookings')

    return render(request, 'travel_options/destination_detail.html', {'destination': travel})
