import requests
import random

import requests

def fetch_user_problems(username):
    solved_problems = set()  # To keep track of solved problems
    difficulties = []  # List to store difficulties of solved problems

    # Fetch solved problems
    url = f'https://codeforces.com/api/user.status?handle={username}&from=1&count=1000'
    response = requests.get(url)
    
    if response.status_code == 200:
        try:
            data = response.json()
            if 'result' not in data:
                return None, None, "username NOT FOUND !"
            submissions = data.get('result', [])
            for submission in submissions:
                problem = submission.get('problem', {})
                contest_id = problem.get('contestId')
                index = problem.get('index')
                verdict = submission.get('verdict')
                rating = problem.get('rating')

                if verdict in ['OK', 'Accepted'] and contest_id and index and rating:
                    problem_id = f"{contest_id}{index}"
                    solved_problems.add(problem_id)
                    difficulties.append(rating)
        except ValueError:
            return None, None, "Error decoding JSON response"
    else:
        return None, None, f"Error fetching solved problems: {response.status_code}"

    # Calculate average difficulty if there are solved problems
    avg_difficulty = sum(difficulties) / len(difficulties) if difficulties else 900

    # Fetch all problems
    url_all_problems = 'https://codeforces.com/api/problemset.problems'
    response_all = requests.get(url_all_problems)
    
    if response_all.status_code == 200:
        try:
            data_all = response_all.json().get('result', {}).get('problems', [])
            problems = []
            for problem in data_all:
                contest_id = problem.get('contestId')
                index = problem.get('index')
                rating = problem.get('rating')
                if contest_id and index and rating and rating >= avg_difficulty - 100 and rating <= avg_difficulty + 200:
                    problem_id = f"{contest_id}{index}"
                    if problem_id not in solved_problems:
                        problem['url'] = f'https://codeforces.com/problemset/problem/{contest_id}/{index}'
                        problems.append(problem)
        except ValueError:
            return None, None, "Error decoding JSON response"
    else:
        return None, None, f"Error fetching all problems: {response_all.status_code}"
    
    return problems, avg_difficulty, None




def fetch_random_problem():
    url = 'https://codeforces.com/api/problemset.problems'
    response = requests.get(url)
    if response.status_code == 200:
        problems = response.json().get('result', {}).get('problems', [])
        if problems:
            return random.choice(problems)
    return None


