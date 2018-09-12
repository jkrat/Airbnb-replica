from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from ..user.models import User
import os

class ListingManager(models.Manager):
    def add_listing(self, data):
        listing_host = User.objects.get(id=data['host'])
        city = data['city']
        listing_1 = Listing(
            name = data['name'],
            listing_type = data['homeType'],
            guests = data['maxguests'],
            bedrooms = data['bedrooms'],
            beds = data['beds'],
            bathrooms = data['bathrooms'],
            description = data['description'],
            city = city.upper(),
            state = data['state'],
            price = data['price'],
            host = listing_host
        )
        listing_1.save()
        return listing_1
        
class Amenity(models.Model):
    name = models.CharField(max_length=255, unique=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Listing(models.Model):
    name = models.TextField(max_length=255)
    listing_type = models.TextField(max_length=255)
    guests = models.IntegerField()
    bedrooms = models.IntegerField()
    beds = models.IntegerField()
    bathrooms = models.IntegerField()
    amenities = models.ManyToManyField(Amenity, related_name = "listing_group")
    description = models.TextField(blank=True)
    city = models.TextField(max_length=255, blank=True)
    state = models.TextField(max_length=255, blank=True)
    price = models.IntegerField(null=True)
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name ='listings')
    rating = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ListingManager()

class Photo(models.Model):
    image = models.ImageField(upload_to='media', default='noProfile.png')
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='photos')
    is_first = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def handle_uploaded_file(file, filename):
    with open('media/' + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

def _delete_file(path):
    if os.path.isfile(path):
        os.remove(path)

def validate_rating(value):
    if 0 > value > 5:
        raise ValidationError(
            _('%(value)s is not in range'),
            params={'value': value},
    )

class Reviews(models.Model):
    title = models.TextField(max_length=255)
    content = models.TextField(max_length=255)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name ='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name ='reviews')
    rating = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
