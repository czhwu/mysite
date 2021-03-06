# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-28 14:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssetDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gdzc', models.CharField(max_length=20, verbose_name='资产编号')),
                ('name', models.CharField(max_length=30, verbose_name='分类')),
                ('discription', models.CharField(max_length=300, verbose_name='描述')),
                ('add_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='入账日期')),
                ('mod_date', models.DateTimeField(auto_now=True, verbose_name='最后更新日期')),
                ('scrap_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='报废日期')),
                ('user', models.CharField(max_length=200, verbose_name='保管员')),
                ('ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='IP地址')),
                ('state', models.CharField(choices=[('SY', '使用'), ('JC', '借出'), ('ZC', '暂存')], default='SY', max_length=2, verbose_name='状态')),
            ],
            options={
                'ordering': ['dpt', 'gdzc'],
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('company', models.CharField(default='苏州中兴联', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Lend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=300)),
                ('lend_time', models.DateTimeField(auto_now=True, verbose_name='借出时间')),
                ('back_time', models.DateTimeField(blank=True, null=True, verbose_name='归还时间')),
                ('user', models.CharField(max_length=200, verbose_name='借用人')),
                ('dpt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.Department')),
                ('gdzc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.AssetDetail')),
            ],
        ),
        migrations.AddField(
            model_name='assetdetail',
            name='dpt',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='assets.Department'),
        ),
    ]
