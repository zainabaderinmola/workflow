from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class GoalStatus(models.Model):
    status_name = models.CharField(max_length = 25)
                                  
    def __str__(self):
        return self.status_name


class ScrumyGoals (models.Model):
    goal_name = models.CharField(max_length = 250)
    goal_id = models.IntegerField(default=1)
    created_by = models.CharField(max_length = 250)
    moved_by = models.CharField(max_length = 250)
    owner = models.CharField(max_length=250)
    user = models.ForeignKey(User, related_name = 'goal_created', on_delete= models.PROTECT)
    goal_status = models.ForeignKey(GoalStatus, on_delete= models.PROTECT)

    #objects = models.Manager()
    class Meta:
        ordering = ('goal_status',)

    def __str__(self):
        return self.goal_name

class ScrumyHistory(models.Model):
    moved_by = models.CharField(max_length = 250)
    created_by = models.CharField(max_length = 250)
    moved_from = models.CharField(max_length = 250)
    moved_to = models.CharField(max_length = 50)
    time_of_action = models.DateTimeField(default = timezone.now)
    goal = models.ForeignKey(ScrumyGoals, on_delete = models.CASCADE)

    def __str__(self):
        return self.created_by
