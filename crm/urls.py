
from django.contrib import admin
from django.urls import path, include
from . import views

#API imports
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'records', views.RecordViewSet)

urlpatterns = [
    path('', views.saludo, name='saludo'),
    path('records/', views.records, name='records'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>', views.costumer_record, name='record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('create_record/', views.create_record, name='create_record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),
    path('api_data', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
