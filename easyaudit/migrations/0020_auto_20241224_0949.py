from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('easyaudit', '0019_alter_crudevent_changed_fields_and_more'),
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
