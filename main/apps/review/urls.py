from django.urls import path
from . import views

urlpatterns = [
    path('<int:listing_id>/new_review', views.new_review, name="new_review"),
    path('fill_reviews', views.fill_reviews, name="fill_reviews")
]