from rest_framework.routers import DefaultRouter

from apps.schedule.views.schedule import ScheduleView

router = DefaultRouter()
router.register(r'current', ScheduleView, basename='schedule')

urlpatterns = router.urls