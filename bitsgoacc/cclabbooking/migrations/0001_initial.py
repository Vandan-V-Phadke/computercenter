# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('date', models.DateField()),
                ('start_hour', models.IntegerField()),
                ('no_of_hours', models.IntegerField()),
                ('user', models.CharField(max_length=30)),
                ('zone1', models.BooleanField(default=False)),
                ('zone2', models.BooleanField(default=False)),
                ('zone3', models.BooleanField(default=False)),
                ('zone4', models.BooleanField(default=False)),
                ('zone5', models.BooleanField(default=False)),
                ('zone6', models.BooleanField(default=False)),
                ('contact_number', models.CharField(max_length=15)),
                ('softwares', models.CharField(max_length=100)),
                ('os', models.CharField(max_length=20)),
                ('lan_required', models.BooleanField(default=True)),
                ('internet_required', models.BooleanField(default=True)),
                ('status', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['date'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Zones_Os',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('zone_number', models.IntegerField()),
                ('os_available', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Zones_Software',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('zone_number', models.IntegerField()),
                ('software_available', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
