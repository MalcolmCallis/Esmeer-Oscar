# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0003_partner_image'),
        ('catalogue', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='partner',
            field=models.ForeignKey(to='partner.Partner', null=True),
            preserve_default=True,
        ),
    ]
