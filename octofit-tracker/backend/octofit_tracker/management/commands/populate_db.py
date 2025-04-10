from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Add test users
        users = [
            User(email='john.doe@example.com', name='John Doe', age=25),
            User(email='jane.smith@example.com', name='Jane Smith', age=30),
        ]
        User.objects.bulk_create(users)

        # Add test teams
        teams = [
            Team(name='Team Alpha', members=['john.doe@example.com', 'jane.smith@example.com']),
        ]
        Team.objects.bulk_create(teams)

        # Add test activities
        activities = [
            Activity(user='john.doe@example.com', activity_type='Running', duration=30),
            Activity(user='jane.smith@example.com', activity_type='Cycling', duration=45),
        ]
        Activity.objects.bulk_create(activities)

        # Add test leaderboard entries
        leaderboard = [
            Leaderboard(user='john.doe@example.com', score=100),
            Leaderboard(user='jane.smith@example.com', score=150),
        ]
        Leaderboard.objects.bulk_create(leaderboard)

        # Add test workouts
        workouts = [
            Workout(name='Morning Run', description='A quick 5km run to start the day'),
            Workout(name='Evening Yoga', description='Relaxing yoga session to end the day'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Database populated with test data'))
