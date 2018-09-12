from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name="landing"),
    path('home/', views.home, name="home"),
    path('<int:listing_id>/listingdetails/', views.listing, name="listing"),
    path('menu/', views.menu, name="menu"),
    path('profile/', views.profile, name="profile"),
    path('becomeHost/', views.becomeHost, name="becomeHost"),
    path('filters/', views.filters, name="filters"),
    path('filterResults/', views.filterResults, name="filterResults"),
    path('searchResults/', views.searchResults, name="searchResults")
]