# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0004_category_partner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='partner',
            field=models.ForeignKey(blank=True, to='partner.Partner', null=True),
            preserve_default=True,
        ),
    ]
