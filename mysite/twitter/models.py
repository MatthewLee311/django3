from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    username = models.CharField(max_length=20)
    post_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.post_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
