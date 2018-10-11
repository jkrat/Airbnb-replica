from django.db import models
from ..listing.models import Listing
from ..user.models import User
 
class TripManager(models.Manager):
    def add_trip(self, data, start_date, end_date, listing_id, user_id):
        listing = Listing.objects.get(id=listing_id)
        user = User.objects.get(id=user_id)
        this_trip = Trip.objects.create(name=data['name'], listing=listing, user=user, start_date=start_date, end_date=end_date)
        return this_trip


class Trip(models.Model):
    name = models.TextField(max_length=255)
    guests = models.ManyToManyField(User, related_name ='invited_trips')
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name ='bookings')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name ='booked_trips')
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TripManager()