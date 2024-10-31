from rest_framework import viewsets, serializers

from apps.schedule.models.schedule import StudentSchedule


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentSchedule
        fields = ['courses']


class ScheduleView(viewsets.ModelViewSet):
    serializer_class = ScheduleSerializer
    queryset = StudentSchedule.objects.all()