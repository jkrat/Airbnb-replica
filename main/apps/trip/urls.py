from django.urls import path
from . import views

urlpatterns = [
    path('<int:listing_id>/create', views.create, name="create")
]