from django.urls import path
from . import views

urlpatterns = [ 
    path('new', views.newListing, name="newListing"),
    path('<int:listing_id>/updatepic/', views.updatepic, name="updatepic"),
    path('<int:listing_id>/delete/', views.delete, name="delete"),
    path('fillamenities', views.fillamenities, name="fillamenities"),
    path('filllistings', views.filllistings, name="filllistings"),
] 