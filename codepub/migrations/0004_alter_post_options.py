# Generated by Django 4.2.3 on 2023-07-20 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codepub', '0003_alter_post_image_alter_post_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['created_at']},
        ),
    ]
