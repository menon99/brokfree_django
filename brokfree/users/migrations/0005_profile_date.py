# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20181110_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='date',
            field=models.CharField(max_length=20, default=datetime.datetime(2018, 11, 10, 19, 28, 46, 805435, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
