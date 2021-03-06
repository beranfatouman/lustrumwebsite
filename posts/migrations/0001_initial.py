# Generated by Django 2.1 on 2018-09-06 22:06

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('lichting', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('count', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('event_date', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Posts',
            },
        ),
        migrations.AddField(
            model_name='amice',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aanwezigen', to='posts.posts'),
        ),
    ]
