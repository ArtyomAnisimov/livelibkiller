# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-21 21:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notificate', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(editable=False, max_length=255, verbose_name='Зарегистрированная модель')),
                ('path', models.CharField(editable=False, max_length=255, verbose_name='Путь к модулю с моделью')),
            ],
            options={
                'db_table': 'registry_models',
            },
        ),
        migrations.AlterModelTable(
            name='notificationsubscribes',
            table='subscriptions',
        ),
    ]
