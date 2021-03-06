# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0005_auto_20150401_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='height',
            field=models.DecimalField(default=0.0, max_digits=5, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='length',
            field=models.DecimalField(default=0.0, max_digits=5, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.DecimalField(default=0.0, max_digits=5, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='width',
            field=models.DecimalField(default=0.0, max_digits=5, decimal_places=2),
            preserve_default=True,
        ),
    ]
