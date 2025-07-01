from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId
from datetime import timedelta
from django.db import connection

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Drop collections directly to avoid issues with primary keys
        with connection.cursor() as cursor:
            cursor.db_conn["octofit_tracker_user"].drop()
            cursor.db_conn["octofit_tracker_team"].drop()
            cursor.db_conn["octofit_tracker_activity"].drop()
            cursor.db_conn["octofit_tracker_leaderboard"].drop()
            cursor.db_conn["octofit_tracker_workout"].drop()

        # Add test data for users
        user1 = User(_id=ObjectId(), username='johndoe', email='john@example.com', password='password123')
        user1.save()
        user2 = User(_id=ObjectId(), username='janesmith', email='jane@example.com', password='password456')
        user2.save()

        # Add test data for teams
        team1 = Team(_id=ObjectId(), name='Team Alpha')
        team1.save()
        team2 = Team(_id=ObjectId(), name='Team Beta')
        team2.save()

        # Add test data for activities
        activity1 = Activity(_id=ObjectId(), user=user1, activity_type='Running', duration=timedelta(minutes=30))
        activity1.save()
        activity2 = Activity(_id=ObjectId(), user=user2, activity_type='Cycling', duration=timedelta(hours=1))
        activity2.save()

        # Add test data for leaderboard
        leaderboard1 = Leaderboard(_id=ObjectId(), user=user1, score=100)
        leaderboard1.save()
        leaderboard2 = Leaderboard(_id=ObjectId(), user=user2, score=80)
        leaderboard2.save()

        # Add test data for workouts
        workout1 = Workout(_id=ObjectId(), name='Morning Run', description='A quick morning run')
        workout1.save()
        workout2 = Workout(_id=ObjectId(), name='Evening Yoga', description='Relaxing yoga session')
        workout2.save()

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
