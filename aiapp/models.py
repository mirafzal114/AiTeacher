from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class FeedBack(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    feedback = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user}:{self.date}"
