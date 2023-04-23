# Generated by Django 4.1.7 on 2023-04-22 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RedSocial', '0007_postseries_publisher'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AddField(
            model_name='postseries',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='posts'),
        ),
    ]
