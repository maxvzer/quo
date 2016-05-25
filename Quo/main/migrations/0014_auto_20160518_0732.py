# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20160518_0730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='faculty',
            field=models.ForeignKey(verbose_name='\u0424\u0430\u043a\u0443\u043b\u044c\u0442\u0435\u0442', to='main.Faculty', null=True),
        ),
    ]
