# Generated by Django 4.2.3 on 2023-08-25 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0003_student_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donation_type', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.IntegerField()),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]