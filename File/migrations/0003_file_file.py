# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-10 21:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('File', '0002_auto_20160810_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='file',
            field=models.FileField(default=2, upload_to='files'),
            preserve_default=False,
        ),
    ]