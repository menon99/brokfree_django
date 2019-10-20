# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='furnishing',
            field=models.CharField(max_length=5, choices=[('Full', 'Fully furnished'), ('Semi', 'Semi furnished'), ('Unfurnished', 'Unfurnished')]),
        ),
    ]
