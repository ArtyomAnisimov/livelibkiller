# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-17 12:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0002_auto_20161210_1353'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookmark',
            options={'ordering': ['date_created'], 'verbose_name': 'Закладка', 'verbose_name_plural': 'Закладки'},
        ),
        migrations.RenameField(
            model_name='bookmark',
            old_name='created',
            new_name='date_created',
        ),
    ]
