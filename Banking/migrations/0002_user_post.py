# Generated by Django 5.0.1 on 2024-02-03 13:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Banking", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="post",
            field=models.CharField(default="Trainee", max_length=10),
            preserve_default=False,
        ),
    ]