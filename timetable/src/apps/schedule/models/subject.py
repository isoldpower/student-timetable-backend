import uuid

from django.db import models

class Subject(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, blank=False, default='')
    description = models.CharField(max_length=500, blank=False, default='')
    creditHours = models.IntegerField(blank=False, default=3)

    def __str__(self):
        return self.title


class StockSubject(models.Model):
    stock_id = models.UUIDField(primary_key=True, blank=False, editable=False, default=uuid.uuid4)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, default='5f5e12bd-2807-4ce8-a260-3405d68dc755')
    location = models.CharField(max_length=100, blank=False)
    time = models.TimeField(blank=False)
    weekdays = models.CharField(max_length=7, blank=False)
    semester = models.CharField(max_length=100, blank=False)