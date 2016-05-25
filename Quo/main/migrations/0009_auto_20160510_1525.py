# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20160510_1510'),
    ]

    operations = [
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.CharField(max_length=255, verbose_name='\u041d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u044f', choices=[(b'1', 1), (b'2', 2)])),
            ],
            options={
                'verbose_name': '\u0413\u043e\u0434 \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u044f',
                'verbose_name_plural': '\u0413\u043e\u0434\u044b \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u044f',
            },
        ),
        migrations.AlterField(
            model_name='person',
            name='address',
            field=models.CharField(default=b'\xd0\x9c\xd0\xbe\xd1\x81\xd0\xba\xd0\xb2\xd0\xb0', max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='birth_place',
            field=models.CharField(default=b' ', max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='birthplace',
            field=models.CharField(default=b'\xd0\x9c\xd0\xbe\xd1\x81\xd0\xba\xd0\xb2\xd0\xb0', max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='document_number',
            field=models.CharField(default=b' ', max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='document_serial_number',
            field=models.CharField(default=b' ', max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='issued_by',
            field=models.CharField(default=b' ', max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='person',
            name='year',
            field=models.ForeignKey(to='main.Year', null=True),
        ),
    ]
