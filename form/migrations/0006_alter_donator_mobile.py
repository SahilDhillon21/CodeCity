# Generated by Django 4.2.3 on 2023-09-11 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0005_donator_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donator',
            name='mobile',
            field=models.CharField(max_length=15),
        ),
    ]
