# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0002_auto_20141007_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='image',
            field=models.ImageField(max_length=255, upload_to=b'images/products/%Y/%m/', null=True, verbose_name='Image', blank=True),
            preserve_default=True,
        ),
    ]
