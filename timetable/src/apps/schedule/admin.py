from django.contrib import admin

from apps.schedule.models.schedule import StudentSchedule

from apps.schedule.models.subject import StockSubject, Subject

# Register your models here.
admin.site.register(Subject)
admin.site.register(StockSubject)
admin.site.register(StudentSchedule)