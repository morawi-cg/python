# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-14 12:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='wercker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TokenName', models.CharField(help_text='name of the wercker token', max_length=30)),
                ('Token', models.CharField(help_text='This is the wercker token', max_length=30)),
            ],
        ),
    ]