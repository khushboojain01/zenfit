from django.shortcuts import render

from .models import GymGear, NutritionSupplement, WorkoutProgram

def gym_gear(request):
    gym_gears = GymGear.objects.all()
    context = {'gym_gears': gym_gears}
    return render(request, 'products/gymgears.html', context)

def nutrition_supplement(request):
    supplements = NutritionSupplement.objects.all()
    context = {'supplements': supplements}
    return render(request, 'products/nutrition_supplements.html', context)

def workout_program(request):
    programs = WorkoutProgram.objects.all()
    context = {'programs': programs}
    return render(request, 'products/workout_programs.html', context)
