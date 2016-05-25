# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20160406_1135'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='faculty',
            options={'verbose_name': '\u0424\u0430\u043a\u0443\u043b\u044c\u0442\u0435\u0442-\u043a\u0430\u0444\u0435\u0434\u0440\u0430-\u0433\u0440\u0443\u043f\u043f\u0430', 'verbose_name_plural': '\u0424\u0430\u043a\u0443\u043b\u044c\u0442\u0435\u0442-\u043a\u0430\u0444\u0435\u0434\u0440\u0430-\u0433\u0440\u0443\u043f\u043f\u0430'},
        ),
        migrations.RemoveField(
            model_name='department',
            name='faculty',
        ),
        migrations.RemoveField(
            model_name='group',
            name='department',
        ),
        migrations.RemoveField(
            model_name='person',
            name='faculty',
        ),
        migrations.AddField(
            model_name='department',
            name='group',
            field=models.ForeignKey(to='main.Group', null=True),
        ),
        migrations.AddField(
            model_name='faculty',
            name='department',
            field=models.ForeignKey(to='main.Department', null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='group',
            field=models.ForeignKey(to='main.Group', null=True),
        ),
    ]
