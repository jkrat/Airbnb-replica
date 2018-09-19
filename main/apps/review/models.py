from django.db import models
from ..listing.models import Listing
from ..user.models import User


class ReviewManager(models.Manager):
    def add_review(self, data, listing_id, user_id):
        listing = Listing.objects.get(id=listing_id)
        user = User.objects.get(id=user_id)
        this_review = Reviews.objects.create(content=data['content'], listing=listing, user=user, rating=int(data['rating']))

        total, count = 0, 0
        for review in listing.reviews.all():
            total += review.rating
            count += 1
        listing.rating = total / count
        listing.save()
        return this_review


class Reviews(models.Model):
    content = models.TextField(max_length=255)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name ='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name ='reviews')
    rating = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ReviewManager()
 