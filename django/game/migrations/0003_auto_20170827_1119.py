# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 09:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_auto_20170827_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='current_turn',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='current_turns', to='game.Player'),
        ),
        migrations.AlterField(
            model_name='board',
            name='won_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='games_won', to='game.Player'),
        ),
        migrations.AlterField(
            model_name='tile',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.Player'),
        ),
    ]
