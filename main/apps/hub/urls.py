from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name="landing"),
    path('home/', views.home, name="home"),
    path('listing/', views.listing, name="listing"),
    path('menu/', views.menu, name="menu"),
    path('profile/', views.profile, name="profile"),
    path('becomeHost/', views.becomeHost, name="becomeHost"),
    path('logout/', views.logout, name="logout"),
    path('login/', views.login, name="login"),
    path('filters/', views.filters, name="filters"),
    path('filterResults/', views.filterResults, name="filterResults"),
    path('searchResults/', views.searchResults, name="searchResults")
]