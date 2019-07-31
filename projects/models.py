from django.db import models
from accounts.models import Team

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    attachment = models.FileField(upload_to='attachments/%Y/%m/%d/', null=True)
    point = models.IntegerField(null=True)
    startdate = models.DateTimeField(null=True)
    deadline = models.DateTimeField(blank=True, null=True)
    team = models.OneToOneField(Team, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.title