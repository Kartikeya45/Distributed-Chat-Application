# Generated by Django 4.2 on 2023-05-01 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Message",
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
                ("sender", models.CharField(max_length=100)),
                ("receiver", models.CharField(max_length=100)),
                ("key", models.CharField(max_length=20)),
                ("body", models.CharField(max_length=1000)),
                ("timestep", models.DateField(auto_now_add=True)),
                ("group", models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name="UserDetails",
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
                ("phone", models.IntegerField()),
                ("password", models.CharField(max_length=100)),
                (
                    "chats",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="authentication.message",
                    ),
                ),
            ],
        ),
    ]