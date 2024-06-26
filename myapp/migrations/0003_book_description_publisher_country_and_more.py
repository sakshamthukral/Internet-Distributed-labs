# Generated by Django 5.0.6 on 2024-05-28 13:32

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0002_member"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="description",
            field=models.TextField(default="No Description Available"),
        ),
        migrations.AddField(
            model_name="publisher",
            name="country",
            field=models.CharField(blank=True, default="USA", max_length=20),
        ),
        migrations.AlterField(
            model_name="member",
            name="address",
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name="member",
            name="city",
            field=models.CharField(default="Windsor", max_length=20),
        ),
        migrations.CreateModel(
            name="order",
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
                (
                    "order_type",
                    models.IntegerField(
                        choices=[(0, "Purchase"), (1, "Borrow")], default=1
                    ),
                ),
                ("date", models.DateField(default=django.utils.timezone.now)),
                ("books", models.ManyToManyField(blank=True, to="myapp.book")),
                (
                    "member",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="orders",
                        to="myapp.member",
                    ),
                ),
            ],
        ),
    ]
