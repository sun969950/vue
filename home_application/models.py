# -*- coding: utf-8 -*-
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    account = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    sex = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    when_created = models.CharField(max_length=50)
    when_modified = models.CharField(max_length=50)

class HostConfig(models.Model):
    host_ip = models.CharField(max_length=50)
    host_name = models.CharField(max_length=50)
    business = models.CharField(max_length=50)
    remark = models.CharField(max_length=50)
    os = models.CharField(max_length=50)
    bk_biz_id = models.CharField(max_length=50)

class Load_Content(models.Model):
    date = models.CharField(max_length=50)
    load_info = models.CharField(max_length=50)
    memory_info = models.CharField(max_length=50)
    disk_info = models.TextField()
    ip = models.CharField(max_length=50)
