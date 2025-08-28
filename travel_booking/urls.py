from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from users import views as user_views
from travel_options import views as travel_views
from bookings import views as bookings_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),

    # User
    path('signup/', user_views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('profile/', user_views.profile, name='profile'),

    # Travel options
    path('', travel_views.destinations_list, name='destinations_list'),
    path('destination/<int:destination_id>/', travel_views.destination_detail, name='destination_detail'),
    # path('destination/<int:destination_id>/book/', travel_views.book_destination, name='book_destination'),

    # Bookings
    path('my_bookings/', bookings_views.my_bookings, name='my_bookings'),
    path('cancel_booking/<int:booking_id>/', bookings_views.cancel_booking, name='cancel_booking'),
]
