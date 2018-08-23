from django.db import models
from ..user.models import User

class Amenity(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Listing(models.Model):
    name = models.TextField(max_length=255)
    listing_type = models.TextField(max_length=255)
    guests = models.IntegerField()
    bedroom = models.IntegerField()
    bed = models.IntegerField()
    bath = models.IntegerField()
    amenities = models.ManyToManyField(Amenity, related_name = "listing_amenities")
    description = models.TextField(blank=True)
    city = models.TextField(max_length=255, blank=True)
    country = models.TextField(max_length=255, blank=True)
    price = models.FloatField(null=True)
    host = models.ForeignKey(User, related_name = 'lister', null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Photo(models.Model):
    image = models.ImageField(upload_to='media', default='noProfile.png')
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='photos')
    is_first = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)





