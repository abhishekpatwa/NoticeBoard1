# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('event_name', models.CharField(max_length=100)),
                ('event_description', models.CharField(max_length=1000)),
                ('event_date', models.DateField()),
                ('event_timing', models.TimeField()),
                ('event_venue', models.CharField(max_length=100)),
                ('event_fees', models.IntegerField(default=0)),
                ('no_of_seat', models.IntegerField(default=56)),
                ('contact_details', models.CharField(max_length=500)),
            ],
        ),
    ]
