# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('audi', '0003_auto_20150127_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingrequest',
            name='ac_required',
            field=models.NullBooleanField(default=None),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bookingrequest',
            name='asset_manager_confirmed',
            field=models.NullBooleanField(default=None),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bookingrequest',
            name='audi_incharge_confirmed',
            field=models.NullBooleanField(default=None),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bookingrequest',
            name='backstage_confirmed',
            field=models.NullBooleanField(default=None),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bookingrequest',
            name='csa_confirmed',
            field=models.NullBooleanField(default=None),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bookingrequest',
            name='pa_required',
            field=models.NullBooleanField(default=None),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bookingrequest',
            name='projector_required',
            field=models.NullBooleanField(default=None),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bookingrequest',
            name='swd_incharge_confirmed',
            field=models.NullBooleanField(default=None),
            preserve_default=True,
        ),
    ]
