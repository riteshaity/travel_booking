from django.urls import path
from . import views

urlpatterns = [
    path("", views.my_bookings, name="my_bookings"),
    path("<int:pk>/cancel/", views.cancel_booking, name="cancel_booking"),
]
