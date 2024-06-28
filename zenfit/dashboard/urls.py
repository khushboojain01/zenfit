from django.urls import path, include
from . import views

urlpatterns = [
    path('accounts/profile/', views.profile, name='profile'),
]