# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20181110_1058'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='first_name',
            new_name='firstname',
        ),
    ]
