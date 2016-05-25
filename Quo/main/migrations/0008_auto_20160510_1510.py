# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20160506_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='birth_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='person',
            name='personal_record',
            field=models.CharField(default=b'\xd0\x9b\xd0\xb8\xd1\x87\xd0\xbd\xd0\xbe\xd0\xb5 \xd0\xb4\xd0\xb5\xd0\xbb\xd0\xbe', max_length=50, null=True, blank=True),
        ),
    ]
