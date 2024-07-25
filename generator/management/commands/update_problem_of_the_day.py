from django.core.management.base import BaseCommand
from generator.utils import fetch_random_problem
from generator.models import ProblemOfTheDay
from datetime import date

class Command(BaseCommand):
    help = 'Update the Problem of the Day'

    def handle(self, *args, **kwargs):
        problem = fetch_random_problem()  # No arguments needed
        if problem:
            # Ensure `contestId` is converted to a string
            contest_id_str = str(problem['contestId'])
            problem_id = contest_id_str + problem['index']
            url = f'https://codeforces.com/problemset/problem/{contest_id_str}/{problem["index"]}'
            
            ProblemOfTheDay.objects.update_or_create(
                date=date.today(),
                defaults={
                    'problem_id': problem_id,
                    'url': url,
                    'name': problem['name'],
                    'difficulty': problem.get('rating', 1500),  # Default to 1500 if rating is not available
                }
            )
            self.stdout.write(self.style.SUCCESS('Successfully updated Problem of the Day'))
        else:
            self.stdout.write(self.style.ERROR('Failed to fetch a random problem'))
