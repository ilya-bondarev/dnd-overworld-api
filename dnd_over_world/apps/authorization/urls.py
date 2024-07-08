from django.urls import path
from apps.authorization import views

urlpatterns = [
    path('', views.auth_index),
    path('registration', views.auth_registration),
]