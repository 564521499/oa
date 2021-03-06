# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-02-14 08:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=16, verbose_name='部门名称')),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=16, verbose_name='职位名称')),
                ('dep_name', models.CharField(max_length=16, verbose_name='部门名称')),
                ('description', models.CharField(max_length=64, verbose_name='职位描述')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.Department')),
            ],
        ),
    ]
