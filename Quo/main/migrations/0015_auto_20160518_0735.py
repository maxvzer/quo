# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20160518_0732'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='faculty',
            options={'verbose_name': '\u0424\u0430\u043a\u0443\u043b\u044c\u0442\u0435\u0442', 'verbose_name_plural': '\u0424\u0430\u043a\u0443\u043b\u044c\u0442\u0435\u0442\u044b'},
        ),
        migrations.AlterField(
            model_name='group',
            name='group',
            field=models.CharField(default=11, max_length=100, verbose_name='\u0413\u0440\u0443\u043f\u043f\u0430'),
        ),
    ]
