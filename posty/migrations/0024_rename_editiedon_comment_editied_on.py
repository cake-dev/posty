# Generated by Django 4.0.7 on 2022-11-23 05:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posty', '0023_comment_editied_comment_editiedon'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='editiedOn',
            new_name='editied_on',
        ),
    ]
