# Generated by Django 4.1.7 on 2023-04-22 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RedSocial', '0002_post_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostJuegos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_del_juego', models.TextField(max_length=20)),
                ('Platamormas', models.TextField(max_length=20)),
                ('Descripcion_del_juego', models.TextField(max_length=500)),
            ],
        ),
    ]
