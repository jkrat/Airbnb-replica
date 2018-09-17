from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user, name="register"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout, name="logout"),
    path('update/', views.update, name="update"),
    path('fillusers', views.fillusers, name="fillusers"),
]