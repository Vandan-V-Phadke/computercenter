# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('audi', '0002_auto_20141118_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingrequest',
            name='uuid_asset',
            field=models.CharField(default=datetime.datetime(2015, 1, 27, 0, 31, 40, 763842, tzinfo=utc), max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookingrequest',
            name='uuid_audi',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookingrequest',
            name='uuid_backstage',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookingrequest',
            name='uuid_csa',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookingrequest',
            name='uuid_swd',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]
