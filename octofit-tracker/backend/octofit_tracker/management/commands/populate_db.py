from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models
from octofit_tracker import models as app_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Cancella dati esistenti
        User = get_user_model()
        User.objects.all().delete()
        Team = app_models.Team
        Team.objects.all().delete()
        Activity = app_models.Activity
        Activity.objects.all().delete()
        Leaderboard = app_models.Leaderboard
        Leaderboard.objects.all().delete()
        Workout = app_models.Workout
        Workout.objects.all().delete()

        # Crea team
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Crea utenti
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password', team=marvel)
        spiderman = User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='password', team=marvel)
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='password', team=dc)
        superman = User.objects.create_user(username='superman', email='superman@dc.com', password='password', team=dc)

        # Crea attività
        Activity.objects.create(user=ironman, type='run', duration=30, distance=5)
        Activity.objects.create(user=spiderman, type='cycle', duration=45, distance=20)
        Activity.objects.create(user=batman, type='swim', duration=25, distance=1)
        Activity.objects.create(user=superman, type='run', duration=60, distance=10)

        # Crea workout
        Workout.objects.create(user=ironman, name='Iron Endurance', description='Long run')
        Workout.objects.create(user=batman, name='Bat Strength', description='Strength training')

        # Leaderboard
        Leaderboard.objects.create(user=ironman, points=100)
        Leaderboard.objects.create(user=spiderman, points=80)
        Leaderboard.objects.create(user=batman, points=90)
        Leaderboard.objects.create(user=superman, points=110)

        self.stdout.write(self.style.SUCCESS('Database popolato con dati di test!'))
