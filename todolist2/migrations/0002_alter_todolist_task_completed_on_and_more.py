# Generated by Django 4.2.7 on 2023-12-01 08:49

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('todolist2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='task_completed_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='task_created_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 1, 14, 19, 41, 871528)),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='taskid',
            field=models.UUIDField(auto_created=True, default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
