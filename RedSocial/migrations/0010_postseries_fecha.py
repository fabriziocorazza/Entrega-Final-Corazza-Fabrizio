# Generated by Django 4.1.7 on 2023-04-23 00:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('RedSocial', '0009_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='postseries',
            name='fecha',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
