# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('stone', '0002_remove_note_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 7, 9, 7, 6, 414000, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
