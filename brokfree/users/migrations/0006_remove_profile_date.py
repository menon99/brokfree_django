# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_profile_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='date',
        ),
    ]
