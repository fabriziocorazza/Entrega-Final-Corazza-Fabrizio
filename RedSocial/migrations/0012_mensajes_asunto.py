# Generated by Django 4.1.7 on 2023-04-23 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RedSocial', '0011_mensajes'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensajes',
            name='asunto',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
