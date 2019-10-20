# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='property',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('lattitude', models.DecimalField(max_digits=8, decimal_places=5)),
                ('longitude', models.DecimalField(max_digits=8, decimal_places=5)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=254)),
                ('location', models.CharField(max_length=30)),
                ('furnishing', models.CharField(max_length=5, choices=[('Full', 'Fully furnished'), ('Semi', 'Semi furnished'), ('Not', 'Unfurnished')])),
                ('facing', models.CharField(max_length=5, choices=[('North', 'North'), ('South', 'South'), ('East', 'East'), ('West', 'West'), ('NA', 'NA')])),
                ('water', models.CharField(max_length=15, choices=[('Corporation', 'Corporation'), ('Borewell', 'Borewell'), ('Both', 'Both'), ('NA', 'NA')])),
                ('bathroom', models.DecimalField(max_digits=1, decimal_places=0)),
                ('bedroom', models.DecimalField(max_digits=1, decimal_places=0)),
                ('security', models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])),
                ('non_veg', models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])),
                ('lift', models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])),
                ('AC', models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])),
                ('swimming_pool', models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])),
                ('servant_room', models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])),
                ('gas_pipe', models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])),
                ('sewage_trt', models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])),
                ('v_parking', models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])),
                ('gym', models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])),
                ('club', models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])),
                ('child_play_area', models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])),
                ('park', models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])),
                ('house_keeping', models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])),
                ('internet', models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])),
                ('intercom', models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])),
                ('fire_safe', models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])),
                ('shopping', models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])),
                ('water_harv', models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])),
                ('power_back', models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])),
                ('rent', models.CharField(max_length=10)),
                ('deposit', models.DecimalField(max_digits=7, decimal_places=0)),
                ('btype', models.CharField(max_length=20)),
                ('tenants', models.CharField(max_length=20)),
                ('possession', models.CharField(max_length=15)),
                ('parking', models.CharField(max_length=20)),
                ('age', models.CharField(max_length=20)),
                ('balcony', models.DecimalField(max_digits=1, decimal_places=0)),
            ],
        ),
    ]
