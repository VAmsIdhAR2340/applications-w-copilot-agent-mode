from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Create test users
        user1 = User.objects.create(email="user1@example.com", name="User One", password="password1")
        user2 = User.objects.create(email="user2@example.com", name="User Two", password="password2")

        # Create test teams
        team1 = Team.objects.create(name="Team Alpha", members=[user1.id, user2.id])

        # Create test activities
        Activity.objects.create(user=user1, type="Running", duration=30)
        Activity.objects.create(user=user2, type="Cycling", duration=45)

        # Create test leaderboard
        Leaderboard.objects.create(team=team1, score=100)

        # Create test workouts
        Workout.objects.create(name="Morning Yoga", description="A relaxing yoga session")
        Workout.objects.create(name="HIIT", description="High-intensity interval training")

        self.stdout.write(self.style.SUCCESS('Database populated with test data'))
