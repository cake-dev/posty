# Generated by Django 4.0.7 on 2022-11-17 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posty', '0020_alter_post_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.CharField(max_length=255),
        ),
    ]