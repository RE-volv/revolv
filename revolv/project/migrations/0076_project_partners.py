# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0075_project_city_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='partners',
            field=ckeditor.fields.RichTextField(help_text=b'This is the content that shows up as a component box on left column on the project page', null=True, verbose_name=b'Project Partners', blank=True),
            preserve_default=True,
        ),
    ]
