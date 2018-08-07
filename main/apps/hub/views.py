from django.shortcuts import render, redirect

def landing(request):
    return render(request, "hub/landing.html")

def home(request):
    return render(request, "hub/dashboard.html")

def login(request):
    return redirect("hub:home")

def logout(request):
    return redirect("hub:home")

def signup(request):
    return redirect("hub:home")

def becomeHost(request):
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
    return render(request, "hub/userProfile.html")

def listing(request):
    return render(request, "hub/ListingProfile.html")
    # return redirect("listingProfile")



