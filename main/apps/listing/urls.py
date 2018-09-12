from django.urls import path
from . import views

urlpatterns = [ 
    path('new', views.newListing, name="newListing"),
    path('amenities', views.newAmenity, name="amenity"),
    path('<int:listing_id>/update/', views.update, name="update"),
    path('<int:listing_id>/review/', views.review, name="review")
] 