from django.urls import path
from .views import HomePageView
from . import views

urlpatterns = [
path('home', HomePageView.as_view(), name='home'),
path('thor', views.thor, name='thor'),
]