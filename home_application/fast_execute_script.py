# -*- coding: utf-8 -*-
import base64
import json
import random
import string
import time

# import paramiko
import requests

from common.log import logger
from conf.default import APP_ID, APP_TOKEN, BK_PAAS_HOST



def fast_execute_script(bk_biz_id, script_content, IP, cloud_id, script_time):
    script_content = base64.urlsafe_b64encode(script_content)
    kwargs = {
        "bk_app_code": APP_ID,
        "bk_app_secret": APP_TOKEN,
        "bk_biz_id": int(bk_biz_id),
        "account": "root",
        "bk_username": "admin",
        "script_content": script_content,
        "script_timeout": script_time,
        "ip_list": [
            {
                "bk_cloud_id": cloud_id,
                "ip": IP
            }]
    }
    url = BK_PAAS_HOST + '/api/c/compapi/v2/job/fast_push_file/'
    result = requests.post(url, data=json.dumps(kwargs))
    content = json.loads(result.content)
    if content["result"]:
        job_instance_id = content["data"]["job_instance_id"]
        res = get_job_instance_status(job_instance_id, bk_biz_id, count=0)
    else:
        res = {"result": False, "data": content["data"]}

    url = BK_PAAS_HOST + '/api/c/compapi/v2/job/fast_execute_script/'
    try:
        result = requests.post(url, data=json.dumps(kwargs))
        content = json.loads(result.content)
        if content["result"]:
            job_instance_id = content["data"]["job_instance_id"]
            res = get_job_instance_status(job_instance_id, bk_biz_id, 0)
            return res
        else:
            res = {"result": "defeated", "data": content}
            return res

    except Exception, e:
        res = {"result": "defeated", "data": e}
        return res
        # count += 1
        # time.sleep(5)
        # if count >= 2:
        #     return "Ssh is failed"
        # return fast_execute_script(bk_biz_id, script_content, IP, cloud_id, count)



def get_job_instance_status(job_instance_id, bk_biz_id, count):   #查询脚本执行状态
    job_instance_id = job_instance_id
    bk_biz_id = bk_biz_id
    data = {
        "bk_app_code": APP_ID,
        "bk_app_secret": APP_TOKEN,
        "bk_username": "admin",
        "job_instance_id": job_instance_id,
        "bk_biz_id": bk_biz_id,
    }
    url = BK_PAAS_HOST + '/api/c/compapi/v2/job/get_job_instance_status/'
    result = requests.post(url, data=json.dumps(data))
    content = json.loads(result.content)

    if content["result"]:
        if content["data"]["is_finished"]:
            job_instance = content["data"]["job_instance"]
            logs = get_job_instance_log(job_instance_id, bk_biz_id, 0)
            if job_instance["status"] == 3:
                res = {"result": True, "data": logs["data"]}
                return res
            else:
                res = {"result": False, "data": logs["data"]}
                return res
        else:
            return get_job_instance_status(job_instance_id, bk_biz_id, 0)
    else:
        count += 1
        time.sleep(5)
        if count < 4:
            get_job_instance_status(job_instance_id, bk_biz_id, count)
        else:
            res = {"result": False, "data": content, "get_job_instance_status": "查询作业执行状态失败"}
            return res


def get_job_instance_log(job_instance_id, bk_biz_id, count): #查询日志信息
    data = {
        "bk_app_code": APP_ID,
        "bk_app_secret": APP_TOKEN,
        "bk_username": "admin",
        "job_instance_id": job_instance_id,
        "bk_biz_id": bk_biz_id,
    }
    url = BK_PAAS_HOST + '/api/c/compapi/v2/job/get_job_instance_log/'
    result = requests.post(url, data=json.dumps(data))
    content = json.loads(result.content)
    if content["result"]:
        log_content = content["data"][0]["step_results"][0]["ip_logs"][0]["log_content"]
        res = {"result": True, "data": log_content}
        return res
    else:
        count += 1
        if count < 5:
            get_job_instance_log(job_instance_id, bk_biz_id, count)
        else:
            res = {"result": False, "data": content, "get_job_instance_log": "查询作业日志失败"}
            return res


def get_agent_status(ip_address, clouds_id):  #查询agent状态
    data = {
        "bk_app_code": APP_ID,
        "bk_app_secret": APP_TOKEN,
        "bk_username": "admin",
        "bk_supplier_id": 0,
        "hosts": [
            {
                "ip": ip_address,
                "bk_cloud_id": clouds_id
            }
        ]
    }
    url = BK_PAAS_HOST + '/api/c/compapi/v2/gse/get_agent_status/'
    result = requests.post(url, data=json.dumps(data))
    content = json.loads(result.content)
    if content["result"]:
        agent_ip = str(clouds_id) + ":%s" % ip_address
        bk_agent_alive = content["data"][agent_ip]["bk_agent_alive"]
        if bk_agent_alive == 1:
            res = {"result": True}
            return res
        elif bk_agent_alive == 0:
            res = {"result": False}
            return res



def search_host(bk_biz_id):    #查询主机信息
    data = {
        "bk_app_code": APP_ID,
        "bk_app_secret": APP_TOKEN,
        'bk_username': "admin",
        "bk_biz_id": bk_biz_id,
        "condition": [
            {
                "bk_obj_id": "host",
                "fields": [],
                "condition": [

                ]
            },
            {
                "bk_obj_id": "biz",
                "fields": [],
                "condition": [
                ]
            }

    ]
    }
    try:
        url = BK_PAAS_HOST + "/api/c/compapi/v2/cc/search_host/"
        result = requests.post(url=url, data=json.dumps(data))
        res = json.loads(result.content)
        if res['result']:
            data = res["data"]["info"]
            lis = []
            for i in data:
                host_content = i["host"]
                biz_content = i["biz"]
                lis.append({"bk_host_name": host_content["bk_host_name"],
                            "bk_host_innerip": host_content["bk_host_innerip"],
                            "bk_os_name": host_content["bk_os_name"],
                            "bk_biz_name": biz_content[0]["bk_biz_name"],
                            })
            res = {"result": True, "data": lis}
            return res
        else:
            res = {"result": False, "data": res}
    except:
        res = {"result": False, "data": "no-know-hostname"}
        return res



def fast_push_file(file_list, bk_cloud_id, IP,  target_path):   #快速分发文件
    search_host_res = search_host(IP)
    if search_host_res["result"]:
        bk_biz_id = int(search_host_res["data"])
        logger.error(bk_biz_id)
        data = {
            "bk_app_code": APP_ID,
            "bk_app_secret": APP_TOKEN,
            "bk_username": "admin",
            "bk_biz_id": bk_biz_id,
            "file_target_path": target_path,  # 文件传输目标路径
            "file_source": [
                {
                    "files": file_list,
                    "account": "root",
                    "ip_list": [
                        {
                            "bk_cloud_id": 0,
                            "ip": "10.150.130.204"
                        },

                    ],
                }
            ],
            "ip_list": [
                {
                    "bk_cloud_id": bk_cloud_id,
                    "ip": IP
                },
            ],
            "account": "root",
        }
        url = BK_PAAS_HOST + '/api/c/compapi/v2/job/fast_push_file/'
        result = requests.post(url, data=json.dumps(data))
        content = json.loads(result.content)
        if content["result"]:
            job_instance_id = content["data"]["job_instance_id"]
            res = get_job_instance_status(job_instance_id, int(search_host_res["data"]), bk_cloud_id)
            return res
        else:
            res = {"result": False, "data": content}
            return res
    else:
        res = {"result": False, "data": search_host_res["data"]}
        return res


def search_business():    #查询蓝鲸平台所有业务
    try:
        data = {
        "bk_app_code": APP_ID,
        "bk_app_secret": APP_TOKEN,
        "bk_username": "admin",
        "bk_supplier_id": 0,
        "fields": [
            "bk_biz_id",
            "bk_biz_name"
        ],
        "page": {
            "start": 0,
            "limit": 200,
            "sort": ""
        }
    }

        url = BK_PAAS_HOST + '/api/c/compapi/v2/cc/search_business/'
        result = requests.post(url, data=json.dumps(data))
        content = json.loads(result.content)
        if content["result"]:
            res = {"result": True, "data": content["data"]["info"]}
            logger.error(res)
            return res
        else:
            res = {"result": False, "data": content}
    except Exception as e:
        logger.error(e)
def random_passwd():

    src = string.ascii_letters + string.digits
    random_passwd = random.sample(src, 7)  # 从字母或数字中随机取7位
    random_passwd.extend(random.choice(['_', '-', ]))
    random_passwd.extend(random.sample(string.digits, 1))
    random_passwd.extend(random.sample(string.ascii_lowercase, 1))
    random_passwd.extend(random.sample(string.ascii_uppercase, 1))
    random_passwd = ''.join(random_passwd)
    return random_passwd

