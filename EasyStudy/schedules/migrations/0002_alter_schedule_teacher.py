# Generated by Django 5.0.6 on 2024-05-22 19:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0001_initial'),
        ('users', '0003_studentprofile_teacherprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='users.teacherprofile'),
        ),
    ]
