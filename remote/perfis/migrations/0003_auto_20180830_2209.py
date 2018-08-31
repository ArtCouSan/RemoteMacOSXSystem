# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0002_computer_userlogin'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Command',
        ),
        migrations.DeleteModel(
            name='Computer',
        ),
    ]
