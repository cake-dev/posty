# Generated by Django 4.1.2 on 2022-11-03 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posty', '0003_upvote_downvote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upvote',
            name='post',
        ),
        migrations.DeleteModel(
            name='downvote',
        ),
        migrations.DeleteModel(
            name='upvote',
        ),
    ]
