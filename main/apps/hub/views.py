from django.shortcuts import render, redirect

def landing(request):
    return render(request, "hub/landing.html")

def home(request):
    return render(request, "hub/dashboard.html")

def login(request):
    return redirect("home")

def signup(request):
    return redirect("home")

def becomeHost(request):
    return redirect("home")



