# Generated by Django 3.1.6 on 2021-05-02 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0008_music_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='music',
            name='album',
        ),
        migrations.RemoveField(
            model_name='music',
            name='singer',
        ),
    ]
