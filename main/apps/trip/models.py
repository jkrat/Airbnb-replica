from django.db import models
from ..listing.models import Listing
from ..user.models import User

class TripManager(models.Manager):
    def add_trip(self, data, listing_id, user_id):
        listing = Listing.objects.get(id=listing_id)
        user = User.objects.get(id=user_id)
        this_trip = Trip.objects.create(name=data['name'], listing=listing, user=user, date_range=data['daterange'])
        return this_trip


class Trip(models.Model):
    name = models.TextField(max_length=255)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name ='bookings')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name ='trips')
    date_range = models.TextField(max_length=255)
    # start_date = models.DateField(auto_now=False, auto_now_add=False)
    # end_date = models.DateField(auto_now=False, auto_now_add=False)
    # duration = models.DurationField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TripManager()