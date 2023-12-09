# Generated by Django 5.0 on 2023-12-09 04:01

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Appointment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("appointment_name", models.CharField(max_length=20)),
                ("appointment_email", models.CharField(max_length=20)),
                ("date", models.DateField()),
                ("appointment_message", models.TextField(blank=True)),
                ("sent_date", models.DateField(auto_now_add=True)),
                ("accepted", models.BooleanField(default=False)),
                ("accepted_date", models.DateField()),
            ],
            options={
                "ordering": ["-accepted"],
            },
        ),
    ]
