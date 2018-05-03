# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-03 06:08
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('AcceptanceCurse', '0003_auto_20180503_0939'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='partner',
        ),
        migrations.AddField(
            model_name='player',
            name='partner_choice',
            field=otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')]),
        ),
        migrations.AddField(
            model_name='player',
            name='partner_id',
            field=otree.db.models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='partner_type',
            field=otree.db.models.IntegerField(null=True),
        ),
    ]