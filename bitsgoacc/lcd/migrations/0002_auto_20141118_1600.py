# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('lcd', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(height_field=b'height', width_field=b'width', upload_to=b'lcd/images/'),
            preserve_default=True,
        ),
    ]
