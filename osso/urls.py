from django.urls import path

from . import views

urlpatterns = [
  path('', views.LoginView.as_view(), name='index'),
  path('profile', views.ProfileView.as_view(), name='profile'),
]