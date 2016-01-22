# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160122_1616'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='body',
            new_name='content',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='snippet',
            field=models.CharField(default=b'', max_length=500, verbose_name='\u6458\u8981'),
            preserve_default=True,
        ),
    ]
