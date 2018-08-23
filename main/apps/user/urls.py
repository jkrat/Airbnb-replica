from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user, name="register"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout, name="logout"),
    path('', views.profile, name="profile"),
    path('update/', views.update, name="update")
    # path('becomeHost/', views.becomeHost, name="becomeHost")
]