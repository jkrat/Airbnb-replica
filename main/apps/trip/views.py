from django.shortcuts import render, redirect
from apps.trip.models import *

def create(request, listing_id):
    user_id = request.session['data']['id']
    this_trip = Trip.objects.add_trip(request.POST, listing_id, user_id)
    return redirect("/{}/listingdetails/".format(listing_id))
