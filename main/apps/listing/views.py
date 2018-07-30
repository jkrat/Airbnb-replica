from django.shortcuts import render, redirect

def newListing(request):
    return redirect("hub:home") 