import datetime
from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    pub_date = models.DateTimeField('date published')
    caption_text = models.CharField(max_length=600)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def __str__(self):
        return self.caption_text
