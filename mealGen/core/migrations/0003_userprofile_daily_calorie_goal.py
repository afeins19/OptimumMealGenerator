# Generated by Django 5.0.4 on 2024-04-22 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_userhealthgoal_daily_calorie_goal_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="daily_calorie_goal",
            field=models.IntegerField(default=2000),
        ),
    ]
