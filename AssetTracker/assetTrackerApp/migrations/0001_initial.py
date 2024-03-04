# Generated by Django 4.2.7 on 2024-03-04 11:09

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Asset",
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
                ("name", models.CharField(max_length=120)),
                ("model", models.CharField(max_length=100)),
                ("brand", models.CharField(max_length=100)),
                (
                    "purchased_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("condition", models.TextField()),
                ("issued", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Company",
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
                ("name", models.CharField(max_length=120)),
                ("location", models.CharField(max_length=120)),
                ("phone", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Employee",
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
                ("name", models.CharField(max_length=120)),
                ("phone", models.IntegerField()),
                ("department", models.CharField(max_length=120)),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="assetTrackerApp.company",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AssetLog",
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
                ("checkout_date", models.DateTimeField()),
                ("return_date", models.DateTimeField(blank=True, null=True)),
                ("checkout_condition", models.TextField()),
                ("return_condition", models.TextField(blank=True, null=True)),
                (
                    "asset",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="assetTrackerApp.asset",
                    ),
                ),
                (
                    "employee",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="assetTrackerApp.employee",
                    ),
                ),
            ],
        ),
    ]
