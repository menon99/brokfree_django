# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20181110_1225'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='firstname',
            new_name='first_name',
        ),
    ]
