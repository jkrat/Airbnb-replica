from django.shortcuts import render, redirect
from apps.trip.models import *
from datetime import datetime

def create(request, listing_id):
    date_range = request.POST['daterange'].split(' - ')
    start_date = datetime.strptime(date_range[0], '%m/%d/%Y')
    end_date = datetime.strptime(date_range[1], '%m/%d/%Y')
    user_id = request.session['data']['id']
    this_trip = Trip.objects.add_trip(request.POST, start_date, end_date, listing_id, user_id)
    return redirect("hub:profile")
 