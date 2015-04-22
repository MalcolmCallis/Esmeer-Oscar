# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0006_auto_20150411_2128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='height',
        ),
        migrations.RemoveField(
            model_name='product',
            name='length',
        ),
        migrations.RemoveField(
            model_name='product',
            name='weight',
        ),
        migrations.RemoveField(
            model_name='product',
            name='width',
        ),
        migrations.AddField(
            model_name='product',
            name='shipping_price',
            field=models.DecimalField(default=0.0, max_digits=6, decimal_places=2),
            preserve_default=False,
        ),
    ]
