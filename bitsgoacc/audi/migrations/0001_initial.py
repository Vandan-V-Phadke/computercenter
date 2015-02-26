# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookingRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.CharField(max_length=25)),
                ('time_of_request', models.DateTimeField(auto_now_add=True)),
                ('time_of_booking', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
