# Generated by Django 2.2.4 on 2019-10-02 15:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20190927_0914'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=300)),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
            options={
                'verbose_name_plural': 'Post',
            },
        ),
        migrations.DeleteModel(
            name='Search',
        ),
    ]
