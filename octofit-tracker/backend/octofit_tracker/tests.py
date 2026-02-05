from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        t = Team.objects.create(name='TestTeam')
        self.assertEqual(str(t), 'TestTeam')
    def test_user_create(self):
        team = Team.objects.create(name='TestTeam')
        u = User.objects.create(name='TestUser', email='test@example.com', team=team)
        self.assertEqual(str(u), 'TestUser')
    def test_activity_create(self):
        team = Team.objects.create(name='TestTeam')
        u = User.objects.create(name='TestUser', email='test@example.com', team=team)
        a = Activity.objects.create(user=u, type='Test', duration=10, date='2026-01-01')
        self.assertEqual(a.type, 'Test')
    def test_workout_create(self):
        w = Workout.objects.create(name='W1', description='desc', suggested_for='Test')
        self.assertEqual(str(w), 'W1')
    def test_leaderboard_create(self):
        team = Team.objects.create(name='TestTeam')
        l = Leaderboard.objects.create(team=team, points=42)
        self.assertEqual(l.points, 42)
