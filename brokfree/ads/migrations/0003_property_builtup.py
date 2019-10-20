# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_auto_20181112_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='builtup',
            field=models.DecimalField(default=0, max_digits=7, decimal_places=0),
        ),
    ]
