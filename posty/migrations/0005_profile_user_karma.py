# Generated by Django 4.1.2 on 2022-11-03 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posty', '0004_remove_upvote_post_delete_downvote_delete_upvote'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user_karma',
            field=models.IntegerField(default=0),
        ),
    ]