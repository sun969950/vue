# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HostConfig',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('host_ip', models.CharField(max_length=50)),
                ('host_name', models.CharField(max_length=50)),
                ('business', models.CharField(max_length=50)),
                ('remark', models.CharField(max_length=50)),
                ('os', models.CharField(max_length=50)),
                ('bk_biz_id', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Load_Content',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.CharField(max_length=50)),
                ('load_info', models.CharField(max_length=50)),
                ('memory_info', models.CharField(max_length=50)),
                ('disk_info', models.TextField()),
                ('ip', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('account', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('sex', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=50)),
                ('when_created', models.CharField(max_length=50)),
                ('when_modified', models.CharField(max_length=50)),
            ],
        ),
    ]
