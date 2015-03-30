# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0003_partner_image'),
        ('catalogue', '0003_remove_category_partner'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='partner',
            field=models.ForeignKey(to='partner.Partner', null=True),
            preserve_default=True,
        ),
    ]
