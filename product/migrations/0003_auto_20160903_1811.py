# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-03 18:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0002_auto_20160903_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200, verbose_name='상품명'),
        ),
        migrations.RemoveField(
            model_name='product',
            name='user',
        ),
        migrations.AddField(
            model_name='product',
            name='user',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='사용자'),
        ),
    ]
