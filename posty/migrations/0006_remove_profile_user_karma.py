# Generated by Django 4.1.2 on 2022-11-03 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posty', '0005_profile_user_karma'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user_karma',
        ),
    ]