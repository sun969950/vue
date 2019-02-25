# -*- coding: utf-8 -*-
"""
celery 任务示例

本地启动celery命令: python  manage.py  celery  worker  --settings=settings
周期性任务还需要启动celery调度命令：python  manage.py  celerybeat --settings=settings
"""
import datetime
import re
import time

from celery import task
from celery.schedules import crontab
from celery.task import periodic_task
from blueking.component.shortcuts import get_client_by_user
from common.log import logger
from home_application.helper import execute_script
from home_application.models import HostConfig, Load_Content


@task()
def async_task(x, y):
    """
    定义一个 celery 异步任务
    """
    logger.error(u"celery 定时任务执行成功，执行结果：{:0>2}:{:0>2}".format(x, y))
    return x + y


def execute_task():
    """
    执行 celery 异步任务

    调用celery任务方法:
        task.delay(arg1, arg2, kwarg1='x', kwarg2='y')
        task.apply_async(args=[arg1, arg2], kwargs={'kwarg1': 'x', 'kwarg2': 'y'})
        delay(): 简便方法，类似调用普通函数
        apply_async(): 设置celery的额外执行选项时必须使用该方法，如定时（eta）等
                      详见 ：http://celery.readthedocs.org/en/latest/userguide/calling.html
    """
    now = datetime.datetime.now()
    logger.error(u"celery 定时任务启动，将在60s后执行，当前时间：{}".format(now))
    # 调用定时任务
    async_task.apply_async(args=[now.hour, now.minute], eta=now + datetime.timedelta(seconds=60))


@periodic_task(run_every=crontab(minute='*/5', hour='*', day_of_week="*"))
def get_time():
    """
    celery 周期任务示例

    run_every=crontab(minute='*/5', hour='*', day_of_week="*")：每 5 分钟执行一次任务
    periodic_task：程序运行时自动触发周期任务
    """
    execute_task()
    now = datetime.datetime.now()
    logger.error(u"celery 周期任务调用成功，当前时间：{}".format(now))



@periodic_task(run_every=crontab(minute='*', hour='*', day_of_week="*"))
def search_loadavg():
    client = get_client_by_user("admin")
    content = HostConfig.objects.all()
    script_content = r"""
#!/bin/bash
cat /proc/loadavg | awk '{print $2}'
echo @@@@@
free -m | awk  'NR == 2 {print $2,$3}'
echo @@@@@
df -h
"""
    for i in content:
        ip = i.host_ip
        res = execute_script(client, int(i.bk_biz_id), script_content, 'root', 1, [{'bk_cloud_id': 0, 'ip': i.host_ip}])
        if res["result"]:
            log_content = res['data'][0]['log_content']
            load_info = log_content.split('@@@@@')[0]
            memory_info = log_content.split('@@@@@')[1]
            log_content = log_content.split('@@@@@')[2].strip().split('\n')[1:]
            disk_info = []
            for i in log_content:
                log_list = re.split(' *',string=i)
                disk_info.append({'Filesystem': log_list[0],
                            'Size': log_list[1],
                            'Used': log_list[2],
                            'Avail': log_list[3],
                            'Use%': log_list[4],
                            'Mounted': log_list[5]})
            time_content = time.strftime('%Y-%m-%d_%H:%M:%S', time.localtime(time.time()))
            Load_Content.objects.create(
                date=time_content,
                load_info=load_info,
                memory_info=memory_info.strip().split(' '),
                disk_info=disk_info,
                ip=ip
            )