# Generated by Django 4.0.7 on 2022-11-16 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posty', '0018_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='onebyone.png', null=True, upload_to='images/'),
        ),
    ]
