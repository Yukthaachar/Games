# views.py
from django.shortcuts import render, redirect
from .forms import InputForm
import random

def Game(request):
    if 'random_number' not in request.session:
        request.session['random_number'] = random.randint(1, 100)
        request.session['count'] = 0

    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            user_number = form.cleaned_data['input']
            request.session['count'] += 1

            random_number = request.session['random_number']
            count = request.session['count']

            if user_number < random_number:
                message = "Too Low"
            elif user_number > random_number:
                message = "Too High"
            else:
                message = f"Correct! You guessed the number in {count} attempts"
                # Reset the game
                request.session['random_number'] = random.randint(1, 100)
                request.session['count'] = 0

            return render(request, 'Game/index.html', {'form': form, 'message': message})

    else:
        form = InputForm()

    return render(request, 'Game/index.html', {'form': form})
