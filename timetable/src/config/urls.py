from django.contrib import admin
from django.urls import path, include

from apps.schedule.urls import urlpatterns as timetable_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/timetable/', include(timetable_urls)),
]
