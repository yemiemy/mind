from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=255)
    totalPoints = models.IntegerField(default=0, null=True, blank=False)
    members = models.ManyToManyField(User, verbose_name='members', null=True)
    program_manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teams', null=True)

    def __str__(self):
        return self.name

class Role(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', null=True, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.username