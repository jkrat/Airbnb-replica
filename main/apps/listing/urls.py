from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.newListing, name="newListing")
]