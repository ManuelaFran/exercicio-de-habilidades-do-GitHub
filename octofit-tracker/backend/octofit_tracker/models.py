from djongo import models

class User(models.Model):
    _id = models.ObjectIdField()
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=128)
    team = models.CharField(max_length=100, blank=True, null=True)
    class Meta:
        db_table = 'users'
        app_label = 'octofit_tracker'

class Team(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100, unique=True)
    members = models.JSONField(default=list)
    class Meta:
        db_table = 'teams'
        app_label = 'octofit_tracker'

class Activity(models.Model):
    _id = models.ObjectIdField()
    user_email = models.EmailField()
    activity_type = models.CharField(max_length=50)
    duration = models.IntegerField()
    date = models.DateField()
    class Meta:
        db_table = 'activity'
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    _id = models.ObjectIdField()
    team = models.CharField(max_length=100)
    points = models.IntegerField()
    class Meta:
        db_table = 'leaderboard'
        app_label = 'octofit_tracker'

class Workout(models.Model):
    _id = models.ObjectIdField()
    user_email = models.EmailField()
    workout_type = models.CharField(max_length=50)
    details = models.JSONField(default=dict)
    date = models.DateField()
    class Meta:
        db_table = 'workouts'
        app_label = 'octofit_tracker'
