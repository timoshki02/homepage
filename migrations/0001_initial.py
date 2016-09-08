# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('image', models.ImageField(upload_to='%y/%m/%d/news')),
                ('title', models.CharField(max_length=250)),
                ('body', models.TextField()),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField()),
                ('status', models.CharField(max_length=10, choices=[('draft', 'Draft'), ('published', 'Published')], default='draft')),
            ],
            options={
                'ordering': ('-publish',),
            },
        ),
    ]
