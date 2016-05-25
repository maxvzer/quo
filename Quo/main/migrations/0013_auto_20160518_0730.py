# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20160511_1410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='group',
        ),
        migrations.RemoveField(
            model_name='faculty',
            name='department',
        ),
        migrations.RemoveField(
            model_name='group',
            name='person',
        ),
        migrations.RemoveField(
            model_name='person',
            name='document_serial_number',
        ),
        migrations.AddField(
            model_name='person',
            name='department',
            field=models.ForeignKey(verbose_name='\u041a\u0430\u0444\u0435\u0434\u0440\u0430', to='main.Department', null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='faculty',
            field=models.ForeignKey(verbose_name='\u0413\u0440\u0443\u043f\u043f\u0430', to='main.Faculty', null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='group',
            field=models.ForeignKey(verbose_name='\u0413\u0440\u0443\u043f\u043f\u0430', to='main.Group', null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='document_number',
            field=models.CharField(default=b' ', max_length=100, null=True, verbose_name='\u0421\u0435\u0440\u0438\u044f \u0438 \u043d\u043e\u043c\u0435\u0440 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430', blank=True),
        ),
        migrations.AlterField(
            model_name='year',
            name='year',
            field=models.CharField(max_length=255, verbose_name='\u0413\u043e\u0434 \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u044f', choices=[(b'1', 1), (b'2', 2), (b'3', 3)]),
        ),
    ]
