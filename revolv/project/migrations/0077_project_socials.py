# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0076_project_partners'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='socials',
            field=ckeditor.fields.RichTextField(help_text=b'This is the content that shows up as a component social media box on left column on the project page', null=True, verbose_name=b'Social Media', blank=True),
            preserve_default=True,
        ),
    ]
