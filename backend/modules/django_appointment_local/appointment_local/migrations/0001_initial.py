# Generated by Django 2.2.28 on 2023-07-31 15:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="AppointmentSession",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("type", models.CharField(max_length=20)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="MeetingInformation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "meeting_type",
                    models.CharField(
                        choices=[
                            ("Message", "Messaging"),
                            ("Voice", "Voice Call"),
                            ("Video", "Video Call"),
                            ("Onsite", "Onsite"),
                        ],
                        default="Message",
                        max_length=10,
                    ),
                ),
                ("meeting_type_detail", models.TextField()),
                ("fees", models.DecimalField(decimal_places=2, max_digits=5)),
                (
                    "service_provider",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="service_provider_fee_info",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Appointment",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("selected_date", models.DateField()),
                ("start_time", models.TimeField()),
                ("end_time", models.TimeField()),
                ("is_available", models.BooleanField(default=False)),
                ("name", models.CharField(max_length=40)),
                ("address", models.CharField(blank=True, max_length=256, null=True)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("age", models.PositiveIntegerField(blank=True, null=True)),
                (
                    "gender",
                    models.CharField(
                        choices=[("Male", "Male"), ("Female", "Female")],
                        default="Male",
                        max_length=7,
                    ),
                ),
                ("add_note", models.TextField(blank=True, null=True)),
                (
                    "appointment_cost",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=6, null=True
                    ),
                ),
                (
                    "additional_fee",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=6, null=True
                    ),
                ),
                (
                    "sub_total",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=6, null=True
                    ),
                ),
                (
                    "discount",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=6, null=True
                    ),
                ),
                (
                    "total",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=6, null=True
                    ),
                ),
                (
                    "appointment_type",
                    models.ManyToManyField(
                        related_name="appointment_meeting_type",
                        to="appointment_local.MeetingInformation",
                    ),
                ),
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="appointment_client",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "service_provider",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="appointment_service_provider",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "session",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="session_appointment",
                        to="appointment_local.AppointmentSession",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
