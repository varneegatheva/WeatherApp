# Generated by Django 4.2.3 on 2023-08-11 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="favouritecity",
            name="city_name",
            field=models.CharField(max_length=100, null=True),
        ),
    ]
