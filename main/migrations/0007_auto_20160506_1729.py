# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20160406_1149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='group',
        ),
        migrations.AddField(
            model_name='group',
            name='person',
            field=models.ForeignKey(to='main.Person', null=True),
        ),
    ]
