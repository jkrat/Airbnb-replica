from django.shortcuts import render, redirect

def profile(request):
    return redirect("hub:home")  