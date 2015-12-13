from django.shortcuts import render

def exercise(request, exercise_id):
    context = {'exercise_id': exercise_id}
    return render(request, 'codes/exercise.html', context)
