from django.db import models

from apps.schedule.models.subject import StockSubject


class StudentSchedule(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    user_id = models.UUIDField(blank=False, editable=False)
    courses = models.ManyToManyField(StockSubject)
