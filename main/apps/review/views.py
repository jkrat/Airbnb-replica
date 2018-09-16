from django.shortcuts import render, redirect
from apps.reveiw.models import *

def index(request):
    return redirect("hub:profile")