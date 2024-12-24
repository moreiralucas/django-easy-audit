# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('easyaudit', '0013_auto_20190723_0126'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='crudevent',
            options={'ordering': ['-datetime'], 'verbose_name': 'Evento do Sistema', 'verbose_name_plural': 'Eventos do Sistema'},
        ),
        migrations.AlterModelOptions(
            name='loginevent',
            options={'ordering': ['-datetime'], 'verbose_name': 'Evento de Login', 'verbose_name_plural': 'Eventos de Login'},
        ),
        migrations.AlterModelOptions(
            name='requestevent',
            options={'ordering': ['-datetime'], 'verbose_name': 'Evento de requisi\xe7\xe3o', 'verbose_name_plural': 'Eventos de requisi\xe7\xe3o'},
        ),
    ]
