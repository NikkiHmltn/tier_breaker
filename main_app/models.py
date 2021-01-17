from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Bracket(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_duration = models.IntegerField()
    end_display = models.CharField(max_length=50)
    public = models.BooleanField(blank=True)
    votes = ArrayField(
        ArrayField(
            models.IntegerField()
        )
    )
    options = ArrayField(
        ArrayField(
            models.CharField(max_length=100)
        )
    )
    def __str__(self):
        return self.title
