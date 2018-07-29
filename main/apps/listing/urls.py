from django.urls import path
from . import views

urlpatterns = [
    path('', views.listing, name="listing")
]