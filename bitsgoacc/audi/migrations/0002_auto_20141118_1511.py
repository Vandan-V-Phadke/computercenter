# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('audi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookingrequest',
            name='time_of_booking',
        ),
        migrations.AddField(
            model_name='bookingrequest',
            name='ac_required',
            field=models.BooleanField(default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bookingrequest',
            name='asset_manager_confirmed',
            field=models.BooleanField(default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bookingrequest',
            name='audi_incharge_confirmed',
            field=models.BooleanField(default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bookingrequest',
            name='backstage_confirmed',
            field=models.BooleanField(default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bookingrequest',
            name='csa_confirmed',
            field=models.BooleanField(default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bookingrequest',
            name='date_of_booking',
            field=models.DateField(default=datetime.datetime(2014, 11, 18, 15, 11, 14, 844427, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookingrequest',
            name='end_time',
            field=models.TimeField(default=datetime.datetime(2014, 11, 18, 15, 11, 25, 444715, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookingrequest',
            name='pa_required',
            field=models.BooleanField(default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bookingrequest',
            name='projector_required',
            field=models.BooleanField(default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bookingrequest',
            name='start_time',
            field=models.TimeField(default=datetime.datetime(2014, 11, 18, 15, 11, 33, 226930, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookingrequest',
            name='swd_incharge_confirmed',
            field=models.BooleanField(default=None),
            preserve_default=True,
        ),
    ]
