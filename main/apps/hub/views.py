from django.shortcuts import render, redirect
from apps.user.models import *

def landing(request):
    return render(request, "hub/landing.html")

def home(request):
    return render(request, "hub/dashboard.html")

def becomeHost(request):
    return render(request, "hub/createListing.html")

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
        return render(request, "hub/userProfile.html", {'user': User.objects.get(id=request.session['data']['id'])} )
    else:
        return redirect("hub:home")

def listing(request):
    return render(request, "hub/ListingProfile.html")
    # return redirect("listingProfile")



