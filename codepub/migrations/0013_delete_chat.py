# Generated by Django 4.2.3 on 2023-08-25 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codepub', '0012_rename_room_chat'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Chat',
        ),
    ]
