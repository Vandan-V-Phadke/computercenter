# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lcd', '0002_auto_20141118_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='image',
            field=models.ImageField(height_field=b'height', width_field=b'width', upload_to=b'lcd/images/'),
            preserve_default=True,
        ),
    ]
