from django.urls import path
from . import views

urlpatterns = [
    path('health/', views.health_check, name='health_check'),
    # Future api routes will go here
]