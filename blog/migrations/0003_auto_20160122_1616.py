# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpost_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='link',
            field=models.CharField(default=b'', help_text="Cool URIs don't change", max_length=150, verbose_name='\u94fe\u63a5'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='publish_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
