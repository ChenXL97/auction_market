# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-17 01:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_privatechat'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='status',
            field=models.CharField(choices=[('review', 'WaitingforReview'), ('pre', 'preparing'), ('in', 'inAuction'), ('end', 'endAuction')], default='review', max_length=18),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='roleofuser',
            name='role',
            field=models.CharField(choices=[('GU', 'general_user'), ('GA', 'goods_administrator')], default='GU', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('0', 'normal'), ('1', 'banned')], default='0', max_length=6),
            preserve_default=False,
        ),
    ]
