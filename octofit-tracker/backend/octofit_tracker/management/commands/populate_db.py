from django.core.management.base import BaseCommand
from octofit_tracker.test_data import test_users, test_teams, test_activities, test_leaderboard, test_workouts
from django.contrib.auth.models import User
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

# Correction du champ 'points' en 'score' pour le modèle Leaderboard

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Create users
        existing_usernames = set(User.objects.values_list('username', flat=True))
        for user_data in test_users:
            if user_data['username'] not in existing_usernames:
                User.objects.create_user(**user_data)

        # Create teams
        for team_data in test_teams:
            Team.objects.create(name=team_data['name'], members=team_data['members'])

        # Create activities
        for activity_data in test_activities:
            user = User.objects.get(username=activity_data['user'])
            Activity.objects.create(user=user, activity_type=activity_data['activity'], duration=activity_data['duration'])

        # Create leaderboard entries
        for leaderboard_data in test_leaderboard:
            user = User.objects.get(username=leaderboard_data['user'])
            Leaderboard.objects.create(user=user, score=leaderboard_data['points'])

        # Create workouts
        for workout_data in test_workouts:
            Workout.objects.create(**workout_data)

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
