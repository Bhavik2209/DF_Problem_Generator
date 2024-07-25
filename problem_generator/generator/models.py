from django.db import models
from django.contrib.auth.models import User
from datetime import date

class ProblemOfTheDay(models.Model):
    problem_id = models.IntegerField()  # The problem ID from Codeforces
    date = models.DateField(default=date.today)
    url = models.URLField()
    name = models.CharField(max_length=255)
    difficulty = models.IntegerField()  # Or any other field you prefer

    def __str__(self):
        return f"Problem of the Day for {self.date}"




class ProblemOfTheDay(models.Model):
    date = models.DateField()
    problem_id = models.CharField(max_length=255)
    url = models.URLField()
    name = models.CharField(max_length=255)
    difficulty = models.IntegerField()

    class Meta:
        unique_together = ('date', 'problem_id')


