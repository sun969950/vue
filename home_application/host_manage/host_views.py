# -*- coding: utf-8 -*-
from __future__ import division
import json
import time
from celery.schedules import crontab
from celery.task import periodic_task

from common.log import logger
from common.mymako import render_json
from home_application.fast_execute_script import search_business, search_host, fast_execute_script
from home_application.models import HostConfig, Load_Content


def search_host_config(request):
    try:
        cond = json.loads(request.body)['condition']
        # return render_json({'result': True, 'data': [{'name': 'wen','id': 5}]})  参数详情
        user = list(HostConfig.objects.filter(host_ip__icontains=cond).all().values())
        return render_json({'result': True, 'data': user})
    except Exception as e:
        logger.exception('search_user error')
        return render_json({'result': False, 'message': e.message})


def search_biz(request):
    try:

        data = search_business()
        # return render_json({'result': True, 'data': [{'name': 'wen','id': 5}]})  参数详情
        return render_json({'result': True, 'data': data["data"]})
    except Exception as e:
        logger.exception('search_biz error')
        return render_json({'result': False, 'message': e.message})


def search_host_list(request):
    body = json.loads(request.body)
    print body

    content = ''
    if body:
        bk_biz_id = body["bk_biz_id"]
        content = search_host(int(bk_biz_id))
        return render_json({'result': True, 'data': content['data']})
    else:
        return render_json({'result': True, 'data': content})


def create_host(request):
    body = json.loads(request.body)
    host_conf = body['host_conf']
    bk_biz_id = body['bk_biz_id']
    remark = body['remark']
    IP = host_conf['bk_host_innerip']
    bk_host_name = host_conf['bk_host_name']
    bk_os_name = host_conf['bk_os_name']
    bk_biz_name = host_conf['bk_biz_name']
    content = HostConfig.objects.filter(host_ip=IP)
    if not content:
        HostConfig.objects.create(
            host_ip=IP,
            host_name=bk_host_name,
            remark=remark,
            os=bk_os_name,
            business=bk_biz_name,
            bk_biz_id=bk_biz_id
        )
        return render_json({"result": True, "data": "创建成功"})
    else:
        return render_json({"result": False, "message": "主机已添加，请勿重复添加"})


def modify_host(request):
    body = json.loads(request.body)
    host_conf = body['item']
    # remark = body['remark']
    IP = host_conf['host_ip']
    try:
        content = HostConfig.objects.filter(host_ip=IP).update(remark=host_conf['remark'])
        return render_json({"result": True, "data": "修改成功"})

    except  Exception as e:
        return render_json({"result": False, "message": "操作失败，请联系管理员"})
    #     return render_json({"result": True, "data": "创建成功"})
    # else:
    #     return render_json({"result": False, "message": "主机已添加，请勿重复添加"})


def delete_host(request):
    try:
        id = request.GET.get('id', None)

        HostConfig.objects.filter(id=id).delete()
        return render_json({'result': True, 'data': None})
    except Exception as e:
        logger.exception('delete_user error')
        return render_json({'result': False, 'message': e.message})


def search_loadavg(request):
    ip = json.loads(request.body)['ip']
    content = Load_Content.objects.filter(ip=ip).order_by('-date')
    lis = content[0:5]
    load_list = []
    for i in lis:
        load_list.append({'name': i.date,'value': i.load_info})
    objects = content[0]
    data = eval(objects.memory_info)
    sums = int(data[0])
    use = int(data[1])
    # memory_list = [{'name': '已使用', 'value': int(str((use / sums) * 100) + '%')},
    #                {'name': '剩余', 'value':int(str((sums - use) / sums * 100) + '%')}]
    disk_list = eval(objects.disk_info)
    memory_list = [{'name': '已使用', 'value': use},
                   {'name': '剩余', 'value': sums-use}]
    return render_json({'result': True,
                        'load': load_list,
                        'memory': memory_list,
                        'disk_list': disk_list})