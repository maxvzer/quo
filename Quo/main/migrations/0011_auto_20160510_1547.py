# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20160510_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='is_learning',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='person',
            name='OKSO',
            field=models.ForeignKey(blank=True, to='main.OKSO', null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='degree',
            field=models.ForeignKey(blank=True, to='main.DegreeOfFitness', null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='grade',
            field=models.ForeignKey(blank=True, to='main.Grade', null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='military',
            field=models.ForeignKey(blank=True, to='main.MilitaryCommissariat', null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='year',
            field=models.ForeignKey(blank=True, to='main.Year', null=True),
        ),
    ]
