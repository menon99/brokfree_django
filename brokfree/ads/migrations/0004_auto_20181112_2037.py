# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_property_builtup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='rent',
            field=models.DecimalField(max_digits=7, decimal_places=0),
        ),
    ]
