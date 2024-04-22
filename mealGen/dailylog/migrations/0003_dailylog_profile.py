# Generated by Django 5.0.4 on 2024-04-22 14:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_userprofile_daily_calorie_goal"),
        ("dailylog", "0002_auto_20240421_1702"),
    ]

    operations = [
        migrations.AddField(
            model_name="dailylog",
            name="profile",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="daily_logs",
                to="core.userprofile",
            ),
        ),
    ]