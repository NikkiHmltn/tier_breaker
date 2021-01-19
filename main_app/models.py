from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Bracket(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_duration = models.IntegerField()
    created_at = models.DateField()
    # winner = models.ForeignKey(BracketOptions) <--- isnt working but not sure if needed since the entire bracket is the key inside bracket_mom maybe??? 
    end_display = models.CharField(max_length=50)
    public = models.BooleanField(default=True)
   
    def __str__(self):
        return self.title

#### attach binary tree to options, vote class of its own
#### binary tree store head node on second class (object)
#### prefer object, see if we can work around dict
#### dont be a dumbass, share the rules to options - votes with partners
class BracketOptions(models.Model):
    bracket_mom = models.ForeignKey(Bracket, on_delete=models.CASCADE)
    votes = ArrayField(models.CharField(max_length=100), blank=True)
    options = ArrayField(models.CharField(max_length=100), blank=True)
    def __str__(self):
        return self.bracket_mom