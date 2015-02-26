# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=1000)),
                ('image', models.ImageField(height_field=b'height', width_field=b'width', upload_to=b'lcd/images/')),
                ('width', models.PositiveIntegerField(null=True, blank=True)),
                ('height', models.PositiveIntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
