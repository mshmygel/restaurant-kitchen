# Generated by Django 5.1.3 on 2024-12-21 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("kitchen", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="dish",
            options={"verbose_name_plural": "Dishes"},
        ),
    ]
