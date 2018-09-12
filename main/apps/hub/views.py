from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from apps.user.models import *
from apps.listing.models import *
import datetime

def landing(request):
    return render(request, "hub/landing.html")

def home(request):
    context = {
        'listings': Listing.objects.all(),
        'range': [1,2,3,4,5]
    }
    return render(request, "hub/dashboard.html", context)

def becomeHost(request):
    if ('data' in request.session):
        return render(request, "hub/createListing.html")
    else:
        return redirect("hub:home")

def filterResults(request):
    return redirect("hub:home")

def searchResults(request):
    return redirect("hub:home")

def menu(request):
    return render(request, "hub/iconButtonNavScreen-loggedin.html")

def filters(request):
    return render(request, "hub/smallScreenFilters.html")

def profile(request):
    if ('data' in request.session):
        user = User.objects.get(id=request.session['data']['id'])
        context = {
            'user': user,
            'reviews': Reviews.objects.filter(user_id=user.id)
        }
        return render(request, "hub/userProfile.html", context )
    else:
        return redirect("hub:home")

def listing(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    reviews = Reviews.objects.filter(listing_id=listing_id)
    context = {
        'listing': listing,
        'amenities': listing.amenities.all(),
        'reviews': reviews,
        'range': [1,2,3,4,5]
    }
    return render(request, "hub/ListingProfile.html", context)
    # return redirect("listingProfile")



