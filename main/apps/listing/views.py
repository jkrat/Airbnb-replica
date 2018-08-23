from django.shortcuts import render, redirect

def newListing(request):
    return redirect("hub:home") 

def home(request):
    return render(request, "hub/dashboard.html")