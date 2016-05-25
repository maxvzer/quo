# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20160510_1547'),
    ]

    operations = [
        migrations.CreateModel(
            name='VUS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('VUS', models.CharField(max_length=255, verbose_name='\u0412\u0423\u0421', choices=[(b'084000', b'084000'), (b'085000', b'085000'), (b'141600', b'141600'), (b'659182', b'659182'), (b'659995', b'659995'), (b'059995', b'059995')])),
            ],
            options={
                'verbose_name': '\u043a\u043e\u0434 \u0412\u0423\u0421',
                'verbose_name_plural': '\u043a\u043e\u0434\u044b \u0412\u0423\u0421',
            },
        ),
        migrations.RemoveField(
            model_name='person',
            name='personal_record',
        ),
        migrations.AlterField(
            model_name='degreeoffitness',
            name='degree_of_fitness',
            field=models.CharField(max_length=255, verbose_name='\u0413\u0440\u0443\u043f\u043f\u0430 \u0437\u0434\u043e\u0440\u043e\u0432\u044c\u044f', choices=[(b'A', '\u0413\u043e\u0434\u0435\u043d'), (b'B', '\u0413\u043e\u0434\u0435\u043d \u0441 \u043d\u0435\u0437\u043d\u0430\u0447\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u043c\u0438 \u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u044f\u043c\u0438'), (b'V', '\u041e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u043d\u043e \u0433\u043e\u0434\u0435\u043d'), (b'G', '\u0412\u0440\u0435\u043c\u0435\u043d\u043d\u043e \u043d\u0435 \u0433\u043e\u0434\u0435\u043d'), (b'D', '\u041d\u0435 \u0433\u043e\u0434\u0435\u043d')]),
        ),
        migrations.AlterField(
            model_name='person',
            name='OKSO',
            field=models.ForeignKey(verbose_name='\u041e\u041a\u0421\u041e', blank=True, to='main.OKSO', null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='address',
            field=models.CharField(default=b'\xd0\x9c\xd0\xbe\xd1\x81\xd0\xba\xd0\xb2\xd0\xb0', max_length=100, null=True, verbose_name='\u0410\u0434\u0440\u0435\u0441\u0441', blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='birth_date',
            field=models.DateField(verbose_name='\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='person',
            name='birth_place',
            field=models.CharField(default=b' ', max_length=100, null=True, verbose_name='\u041c\u0435\u0441\u0442\u043e \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f', blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='birthplace',
            field=models.CharField(default=b'\xd0\x9c\xd0\xbe\xd1\x81\xd0\xba\xd0\xb2\xd0\xb0', max_length=100, null=True, verbose_name='\u041c\u0435\u0441\u0442\u043e \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f', blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='degree',
            field=models.ForeignKey(verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f \u0433\u043e\u0434\u043d\u043e\u0441\u0442\u0438', blank=True, to='main.DegreeOfFitness', null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='document_number',
            field=models.CharField(default=b' ', max_length=100, null=True, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430', blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='document_serial_number',
            field=models.CharField(default=b' ', max_length=100, null=True, verbose_name='\u0421\u0435\u0440\u0438\u044f \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430', blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(default=b'\xd0\x98\xd0\xbc\xd1\x8f', max_length=100, verbose_name='\u0418\u043c\u044f'),
        ),
        migrations.AlterField(
            model_name='person',
            name='grade',
            field=models.ForeignKey(verbose_name='\u0412\u043e\u0435\u043d\u043a\u043e\u043c\u0430\u0442', blank=True, to='main.Grade', null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='is_learning',
            field=models.BooleanField(default=False, verbose_name='\u041e\u0431\u0443\u0447\u0430\u0435\u0442\u0441\u044f \u043b\u0438 \u043d\u0430 \u0432\u043e\u0435\u043d\u043d\u043e\u0439 \u043a\u0430\u0444\u0435\u0434\u0440\u0435?'),
        ),
        migrations.AlterField(
            model_name='person',
            name='issued_by',
            field=models.CharField(default=b' ', max_length=100, null=True, verbose_name='\u0412\u044b\u0434\u0430\u043d', blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(default=b'\xd0\xa4\xd0\xb0\xd0\xbc\xd0\xb8\xd0\xbb\xd0\xb8\xd1\x8f', max_length=100, verbose_name='\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e'),
        ),
        migrations.AlterField(
            model_name='person',
            name='middle_name',
            field=models.CharField(default=b'\xd0\x9e\xd1\x82\xd1\x87\xd0\xb5\xd1\x81\xd1\x82\xd0\xb2\xd0\xbe', max_length=100, verbose_name='\u0424\u0430\u043c\u0438\u043b\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='person',
            name='military',
            field=models.ForeignKey(verbose_name='\u0412\u043e\u0435\u043d\u043a\u043e\u043c\u0430\u0442', blank=True, to='main.MilitaryCommissariat', null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='year',
            field=models.ForeignKey(verbose_name='\u0413\u043e\u0434 \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u044f', blank=True, to='main.Year', null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='VUS',
            field=models.ForeignKey(verbose_name='\u0412\u0423\u0421', blank=True, to='main.VUS', null=True),
        ),
    ]
