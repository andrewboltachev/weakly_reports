# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeentry',
            name='project',
            field=models.ForeignKey(default=None, to='reports.Project'),
            preserve_default=False,
        ),
    ]
