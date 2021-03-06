# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-04-26 04:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('song', models.CharField(max_length=200)),
                ('onset', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('pitch', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('volume', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('duration', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('channel', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('avg_rating', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('note', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='termproject.Note')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=200)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
