# Generated by Django 4.2.3 on 2023-08-15 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_favouritecity_city_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="favouritecity",
            name="city_name",
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]
