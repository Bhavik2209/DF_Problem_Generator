from django.shortcuts import render
from .forms import UsernameForm
from .utils import fetch_user_problems
import random
from generator.models import ProblemOfTheDay
from datetime import date

def generate_problem_set(request):
    problems = []
    avg_difficulty = None
    problem_of_the_day = ProblemOfTheDay.objects.filter(date=date.today()).first()

    if request.method == 'POST':
        form = UsernameForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            problems, avg_difficulty = fetch_user_problems(username)
            
            if problems:
                num_problems = min(len(problems), 10)  # Limit to 10 problems or the number of problems available
                problems = random.sample(problems, num_problems)
            else:
                problems = []
                avg_difficulty = None  # No problems to show
    else:
        form = UsernameForm()

    return render(request, 'generator.html', {
        'form': form,
        'problems': problems,
        'avg_difficulty': avg_difficulty,
        'problem_of_the_day': problem_of_the_day,
    })
