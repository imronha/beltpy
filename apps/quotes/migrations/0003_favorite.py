# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-22 00:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0002_auto_20170721_2356'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('fav_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fav_by', to='quotes.User')),
                ('fav_quote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fav_quote', to='quotes.Quote')),
            ],
        ),
    ]
