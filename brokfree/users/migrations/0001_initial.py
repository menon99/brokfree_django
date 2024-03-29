# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('first_name', models.CharField(max_length=30, blank=True, null=True)),
                ('last_name', models.CharField(max_length=30, blank=True, null=True)),
                ('mobile', models.IntegerField()),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL,on_delete=models.CASCADE)),
            ],
        ),
    ]
