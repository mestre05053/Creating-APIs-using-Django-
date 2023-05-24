from django.urls import path, include
from .views import HomePageView, AboutPageView
from . import views

urlpatterns = [
    path('home/', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('thor/', views.thor, name='thor'),
]