from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Poll(models.Model):
    question = models.TextField()
    option_one = models.CharField(max_length=30)
    option_two = models.CharField(max_length=30)
    option_three = models.CharField(max_length=30)
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)
    deadline = models.DateTimeField(null=True, blank=True)

    def total(self):
        return self.option_one_count + self.option_two_count + self.option_three_count

    def is_active(self):
        if self.deadline:
            return self.deadline > timezone.now()
        else:
            return True

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.poll.deadline and not self.poll.is_active():
            raise ValueError("Voting is closed for this poll.")
        super().save(*args, **kwargs)
