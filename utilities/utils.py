# -*- coding:utf-8 -*-
import datetime
import json
from common.mymako import render_json


# 获取当前时间 年-月-日 时:分:秒
def get_time_now_str():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# 获取当前日期 年-月-日
def get_date_now_str():
    return datetime.datetime.now().strftime("%Y-%m-%d")


# DateTimeField格式化
class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)


def datetime_cover_str(item):
    obj = {}
    if item.has_key('_id'):
        del item['_id']
    for k in item:
        if isinstance(item[k], datetime.datetime):
            obj[k] = item[k].strftime('%Y-%m-%d %H:%M:%S')
        else:
            obj = item
    return obj


# 成功返回数据
def success_result(data='', *args, **kwargs):
    result = {
        'result': True,
        'data': data
    }
    for arg in args:
        result = dict(result, **arg)
    result = dict(result, **kwargs)
    return render_json(result)


# 失败返回数据
def fail_result(message='', *args, **kwargs):
    if not message:
        message = u'系统异常,请联系管理员'
    result = {
        'result': False,
        'message': message
    }
    for arg in args:
        result = dict(result, **arg)
    result = dict(result, **kwargs)
    return render_json(result)


def get_all_page_count(data_count, PAGE_SIZE):
    c = data_count / PAGE_SIZE if data_count % PAGE_SIZE == 0 else data_count / PAGE_SIZE + 1
    return 1 if c == 0 else c


def get_page_data(cursor, page_num=1, page_size=10):
    return cursor[(page_num - 1) * page_size: page_size * page_num]

