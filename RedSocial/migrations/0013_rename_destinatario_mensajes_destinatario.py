# Generated by Django 4.1.7 on 2023-04-23 01:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RedSocial', '0012_mensajes_asunto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mensajes',
            old_name='destinatario',
            new_name='Destinatario',
        ),
    ]
