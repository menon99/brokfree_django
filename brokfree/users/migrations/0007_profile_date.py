# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_profile_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='date',
            field=models.CharField(max_length=20, blank=True, null=True),
        ),
    ]
