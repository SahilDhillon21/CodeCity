# Generated by Django 4.2.3 on 2023-08-10 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codepub', '0010_rename_reports_report'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]
