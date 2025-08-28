from django.urls import path
from . import views

urlpatterns = [
    path("", views.destinations_list, name="destinations_list"),
    path("<int:pk>/", views.destination_detail, name="destination_detail"),
    # Travel options
    # path('destination/<int:destination_id>/book/', views.book_destination, name='book_destination'),
 
]
