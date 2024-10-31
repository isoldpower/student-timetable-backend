from rest_framework import serializers

from apps.schedule.models.subject import Subject, StockSubject


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class StockSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockSubject
        fields = '__all__'
        read_only_fields = ('id', 'title', 'description', 'creditHours')