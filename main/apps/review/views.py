from django.shortcuts import render, redirect
from apps.review.models import *
from apps.listing.models import Listing
from apps.user.models import User
from random import randint

def index(request):
    return redirect("hub:profile")

def new_review(request, listing_id):
    user_id = request.session['data']['id']
    this_review = Reviews.objects.add_review(request.POST, listing_id, user_id)
    return redirect("/{}/listingdetails/".format(listing_id))


# ----------------------------- dev tools - fill random data --------------------------------#

reveiws_list = [
    "This Lodging option was better than I expected. Everything was very easy to understand and my stay was smooth. The location is fantastic and one can walk to places to eat and drink. I will stay there again.", 
    "The place is pleasant place to cool your heels after a busy day in downtown. The neighborhood is quiet and there is enough privacy for you to chill for an evening. I will stay there again if the opportunity arises.", "My host was great and very prompt to reply to any questions that we had.  The cottage is an oasis of relaxation and the next time we return to the area we'll definitely try and stay there again.", 
    "Great location and excellently designed space. Loved how functional and comfortable they had made the small space. We were able to walk to a couple of the host's local reconmendations and both were great!", 
    "Great place with great people. Has all the things you need to make it feel like a home away from home", "Super comfortable, great backyard patio, awesome neighborhood!!", 
    "We could not have asked for a better host, and along with the delicious weather, we had the most comfortable, cozy and delightful place to stay. Highly recommend!", 
    "This Air Bnb was the perfect place for me to stay on my solo trip! The town was so beautiful, lots to do around there and walkable! It was also very close to downtown which was great because I used uber while I was visiting. I would definitely recommend this to anyone wanting a homey vibe while on vacation!", 
    "I loved staying at the this place. I was able to walk to the nearby yoga studio, restaurants, shops, etc. The cottage felt very private and had everything I needed to make my stay enjoyable.", 
    "I only stayed for one night on a quick trip but I hope to return again! The cottage had everything I needed, a very comfortable bed, and a great outdoor space. Coffee and restaurants were just around the corner.", 
    "I loved the little place. It was warm and cozy and had everything you would want for an extended stay. I was right in town, where I wanted to be, and it was easy to walk, drive, or Lyft where I needed to go. What a fantastic host! Very quick to respond and checked in with me during my stay. Thanks!",
    "My first venture using Airbnb lead me to an amazing place. I found the owner very      accommodating and very quick to respond to our spontaneous request. The location is walking distance to restaurants and shops. The place exceeded our needs. Cute, clean, and perfect location.", 
    "This condo has a great location with ski in ski out access and a close walk to town. The beds were not terribly comfortable for me, my husband slept ok but I need a firm bed and the main bed was very very soft so beware.  There is a nice view of aspen trees but no balcony etc. So if you are looking for an alternative to a hotel then a good find.", 
    "Truly wonderful spot for a couples getaway! Perfect location between town and the outdoors. Ten minute walk to downtown and a hiking trail right out the side door. Very clean and has great hot tubs/ spa on the property. Would certainly stay here again!", 
    "Just as described! Perfect little studio, clean, and great location. Wish the weather would have been a notch cooler for us, as AC’s are not a thing in the mountains :) great place!", 
    "Terrific location. Great hike right outside building. Cozy stay!", 
    "Perfect spot for a quiet getaway. A half mile from downtown. Garage for vehicle. Worth it. We will return.", 
    "The location was amazing! At the steps of everything. The apartment was comfortable for the two of us, we had everything we needed for a great weekend. The bed was super comfortable, and with the bedding it was really warm despite it being 9 degrees outside!", 
    "Jack and Jerrod were very helpful! This studio was perfect for our 2 days of skiing at skiing! Location is excellent, across the street from Peak 9 lift, and within blocks of everything you need to walk to. We did not use our car once after arriving. Very comfy." ]

def fill_reviews(request):
    listing_list = Listing.objects.all()
    user_list = User.objects.all()
    for user in user_list:
        listing_id = listing_list[randint(0, len(listing_list) - 1)].id
        user_id = user.id
        data = {
            "content": reveiws_list[randint(0, len(reveiws_list) - 1)],
            "rating": randint(2,5)
        }
        this_review = Reviews.objects.add_review(data, listing_id, user_id)
    return redirect("hub:profile")