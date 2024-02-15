# Generated by Django 4.2.7 on 2023-12-01 08:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoList',
            fields=[
                ('taskid', models.UUIDField(auto_created=True, primary_key=True, serialize=False)),
                ('task_title', models.TextField(max_length=225)),
                ('task_description', models.TextField(null=True)),
                ('task_created_on', models.DateTimeField(default=datetime.datetime.now)),
                ('task_completed_on', models.DateTimeField()),
            ],
        ),
    ]
