# Generated by Django 4.1.2 on 2022-11-10 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posty', '0014_alter_comment_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.CharField(max_length=250),
        ),
    ]
