from django.urls import path
from . import views

urlpatterns = [ 
    path('new', views.newListing, name="newListing"),
    path('amenities', views.newAmenity, name="amenity"),
] 