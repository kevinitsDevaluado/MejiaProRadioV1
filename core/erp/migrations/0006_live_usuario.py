# Generated by Django 3.1.6 on 2021-04-30 23:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('erp', '0005_auto_20210429_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='live',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.user', verbose_name='usuario'),
            preserve_default=False,
        ),
    ]
