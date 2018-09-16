from django.shortcuts import render, redirect
from apps.trip.models import *

def index(request):
    return redirect("hub:profile")