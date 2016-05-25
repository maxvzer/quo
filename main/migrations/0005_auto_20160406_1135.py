# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20160317_1052'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='degreeoffitness',
            options={'verbose_name': '\u0413\u0440\u0443\u043f\u043f\u0430 \u0437\u0434\u043e\u0440\u043e\u0432\u044c\u044f', 'verbose_name_plural': '\u0413\u0440\u0443\u043f\u043f\u044b \u0437\u0434\u043e\u0440\u043e\u0432\u044c\u044f'},
        ),
        migrations.AlterModelOptions(
            name='department',
            options={'verbose_name': '\u041a\u0430\u0444\u0435\u0434\u0440\u0430', 'verbose_name_plural': '\u041a\u0430\u0444\u0435\u0434\u0440\u044b'},
        ),
        migrations.AlterModelOptions(
            name='faculty',
            options={'verbose_name': '\u0424\u0430\u043a\u0443\u043b\u044c\u0442\u0435\u0442', 'verbose_name_plural': '\u0424\u0430\u043a\u0443\u043b\u044c\u0442\u0435\u0442\u044b'},
        ),
        migrations.AlterModelOptions(
            name='grade',
            options={'verbose_name': '\u041d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u044f', 'verbose_name_plural': '\u041d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u044f'},
        ),
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': '\u0413\u0440\u0443\u043f\u043f\u0430', 'verbose_name_plural': '\u0413\u0440\u0443\u043f\u043f\u044b'},
        ),
        migrations.AlterModelOptions(
            name='militarycommissariat',
            options={'verbose_name': '\u0412\u043e\u0435\u043d\u043a\u043e\u043c\u0430\u0442', 'verbose_name_plural': '\u0412\u043e\u0435\u043d\u043a\u043e\u043c\u0430\u0442\u044b'},
        ),
        migrations.AlterModelOptions(
            name='okso',
            options={'verbose_name': '\u043a\u043e\u0434 \u041e\u041a\u0421\u041e', 'verbose_name_plural': '\u043a\u043e\u0434\u044b \u041e\u041a\u0421\u041e'},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': '\u0421\u0442\u0443\u0434\u0435\u043d\u0442', 'verbose_name_plural': '\u0421\u0442\u0443\u0434\u0435\u043d\u0442\u044b'},
        ),
        migrations.RemoveField(
            model_name='department',
            name='group',
        ),
        migrations.RemoveField(
            model_name='faculty',
            name='department',
        ),
        migrations.AddField(
            model_name='department',
            name='faculty',
            field=models.ForeignKey(to='main.Faculty', null=True),
        ),
        migrations.AddField(
            model_name='group',
            name='department',
            field=models.ForeignKey(to='main.Department', null=True),
        ),
        migrations.AlterField(
            model_name='degreeoffitness',
            name='degree_of_fitness',
            field=models.CharField(max_length=255, verbose_name='\u0413\u0440\u0443\u043f\u043f\u0430 \u0437\u0434\u043e\u0440\u043e\u0432\u044c\u044f', choices=[(b'A1', '\u04101'), (b'A2', '\u04102'), (b'A3', '\u04103'), (b'B1', '\u04111'), (b'B2', '\u04112'), (b'B3', '\u04113'), (b'B4', '\u04114'), (b'V', '\u0412'), (b'G', '\u0413'), (b'D', '\u0414')]),
        ),
        migrations.AlterField(
            model_name='okso',
            name='OKSO',
            field=models.CharField(max_length=255, verbose_name='\u041e\u041a\u0421\u041e'),
        ),
    ]
