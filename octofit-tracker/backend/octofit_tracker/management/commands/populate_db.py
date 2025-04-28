from django.core.management.base import BaseCommand
from djongo import models
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date

class Command(BaseCommand):
    help = 'Popula o banco octofit_db com dados de teste para users, teams, activity, leaderboard e workouts.'

    def handle(self, *args, **kwargs):
        # Usuários
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        user1 = User.objects.create(email='alice@octofit.com', name='Alice', password='senha123', team='Team A')
        user2 = User.objects.create(email='bob@octofit.com', name='Bob', password='senha123', team='Team A')
        user3 = User.objects.create(email='carol@octofit.com', name='Carol', password='senha123', team='Team B')
        user4 = User.objects.create(email='dave@octofit.com', name='Dave', password='senha123', team='Team B')

        team_a = Team.objects.create(name='Team A', members=[user1.email, user2.email])
        team_b = Team.objects.create(name='Team B', members=[user3.email, user4.email])

        Activity.objects.create(user_email=user1.email, activity_type='run', duration=30, date=date(2025, 4, 1))
        Activity.objects.create(user_email=user2.email, activity_type='walk', duration=45, date=date(2025, 4, 2))
        Activity.objects.create(user_email=user3.email, activity_type='bike', duration=60, date=date(2025, 4, 3))
        Activity.objects.create(user_email=user4.email, activity_type='swim', duration=25, date=date(2025, 4, 4))

        Leaderboard.objects.create(team='Team A', points=75)
        Leaderboard.objects.create(team='Team B', points=85)

        Workout.objects.create(user_email=user1.email, workout_type='cardio', details={'distance': 5}, date=date(2025, 4, 1))
        Workout.objects.create(user_email=user2.email, workout_type='strength', details={'reps': 20}, date=date(2025, 4, 2))
        Workout.objects.create(user_email=user3.email, workout_type='yoga', details={'duration': 60}, date=date(2025, 4, 3))
        Workout.objects.create(user_email=user4.email, workout_type='cardio', details={'distance': 3}, date=date(2025, 4, 4))

        self.stdout.write(self.style.SUCCESS('Banco octofit_db populado com dados de teste!'))
