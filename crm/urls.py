"""
URL configuration for asistencia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

#API imports
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'records', views.RecordViewSet)

urlpatterns = [
    path('', views.saludo, name='saludo'),
    path('json/', views.json, name='json'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>', views.costumer_record, name='record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('create_record/', views.create_record, name='create_record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),
    path('api_data', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

handler404 = "crm.views.page_not_found_view"