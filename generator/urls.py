from django.urls import path
from .views import generate_problem_set

urlpatterns = [
    path('', generate_problem_set, name='generate_problem_set'),
]
