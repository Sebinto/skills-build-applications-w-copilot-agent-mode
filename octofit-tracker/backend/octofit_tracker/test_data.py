# Données de test pour la base de données octofit_db

test_users = [
    {"username": "john_doe", "email": "john@example.com", "password": "password123"},
    {"username": "jane_smith", "email": "jane@example.com", "password": "password123"},
]

test_teams = [
    {"name": "Team Alpha", "members": ["john_doe", "jane_smith"]},
    {"name": "Team Beta", "members": []},
]

test_activities = [
    {"user": "john_doe", "activity": "Running", "duration": 30, "calories_burned": 300},
    {"user": "jane_smith", "activity": "Cycling", "duration": 45, "calories_burned": 400},
]

test_leaderboard = [
    {"user": "john_doe", "points": 100},
    {"user": "jane_smith", "points": 120},
]

test_workouts = [
    {"name": "Morning Run", "description": "A quick 5km run to start the day."},
    {"name": "Evening Yoga", "description": "Relaxing yoga session to wind down."},
]
