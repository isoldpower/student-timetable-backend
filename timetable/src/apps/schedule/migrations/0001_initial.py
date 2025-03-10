# Generated by Django 4.2.16 on 2024-10-31 12:46

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=100)),
                ('description', models.CharField(default='', max_length=500)),
                ('creditHours', models.IntegerField(default=3)),
            ],
        ),
        migrations.CreateModel(
            name='StockSubject',
            fields=[
                ('subject_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='schedule.subject')),
                ('stock_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=100)),
                ('time', models.TimeField()),
                ('weekdays', models.CharField(max_length=7)),
                ('semester', models.CharField(max_length=100)),
            ],
            bases=('schedule.subject',),
        ),
        migrations.CreateModel(
            name='StudentSchedule',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('user_id', models.UUIDField(editable=False)),
                ('courses', models.ManyToManyField(to='schedule.stocksubject')),
            ],
        ),
    ]
