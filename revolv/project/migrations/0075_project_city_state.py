# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0074_auto_20200221_1624'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='city_state',
            field=models.CharField(help_text=b'City and State of the project?', max_length=255, null=True, verbose_name=b'Project City and State', blank=True),
            preserve_default=True,
        ),
    ]
