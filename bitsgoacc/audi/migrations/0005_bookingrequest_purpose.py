# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('audi', '0004_auto_20150127_0054'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingrequest',
            name='purpose',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
