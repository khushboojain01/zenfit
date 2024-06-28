from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('gym-gear/', views.gym_gear, name='gym_gear'),
    path('nutrition-supplements/', views.nutrition_supplement, name='nutrition_supplement'),
    path('workout-programs/', views.workout_program, name='workout_program'),
    
]