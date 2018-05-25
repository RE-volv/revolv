# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0029_auto_20180328_0819'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectmontlyrepaymentconfig',
            name='starting_month',
            field=models.CharField(default=b'May', max_length=25),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='projectmontlyrepaymentconfig',
            name='starting_year',
            field=models.IntegerField(default=2018, max_length=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='projectmontlyrepaymentconfig',
            name='repayment_type',
            field=models.CharField(blank=True, max_length=3, choices=[(b'SSF', b'Solar Seed Fund'), (b'REV', b'RE-volv Overhead')]),
            preserve_default=True,
        ),
    ]
