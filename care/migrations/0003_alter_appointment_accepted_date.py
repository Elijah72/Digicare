# Generated by Django 5.0 on 2023-12-09 04:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("care", "0002_appointment_appointment_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appointment",
            name="accepted_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]
