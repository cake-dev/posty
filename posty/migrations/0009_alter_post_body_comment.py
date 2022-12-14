# Generated by Django 4.1.2 on 2022-11-10 19:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posty', '0008_upvoted_downvoted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.CharField(max_length=300),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('comment_karma', models.IntegerField(blank=True, default=0, null=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='comments', to='posty.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
