# -*-coding:utf-8-*-

from blueking.component.shortcuts import get_client_by_user
from conf.default import APP_ID, APP_TOKEN
import base64
import time


# 操作作业平台快速执行脚本
def execute_script(client, biz_id, script_content, account, script_type, ip_list):
    kwargs = {
        "bk_biz_id": biz_id,
        "script_content": base64.b64encode(script_content),
        "script_timeout": 60,
        "account": account,
        "script_type": script_type,
        "ip_list": ip_list
    }
    res = client.job.fast_execute_script(**kwargs)
    if res['result']:
        time.sleep(3)
        job_instance_id = res['data']['job_instance_id']
        result = get_job_instance_log(client, biz_id, job_instance_id)
        return result
    else:
        return {'result': False, 'message': res['message']}


# 获取脚本任务Log
def get_job_instance_log(client, biz_id, job_instance_id):
    kwargs = {
        "bk_biz_id": biz_id,
        "job_instance_id": job_instance_id
    }
    res = client.job.get_job_instance_log(**kwargs)
    if res['result']:
        step = res['data'][0]
        if step['is_finished']:
            ip_logs = []
            is_success = step['step_results'][0]['ip_status'] == 9
            for step_result in step['step_results'][0]['ip_logs']:
                ip_log = {
                    'is_success': is_success,
                    'bk_cloud_id': step_result['bk_cloud_id'],
                    'ip': step_result['ip'],
                    'log_content': step_result['log_content']
                }
                ip_logs.append(ip_log)
            return {'result': True, 'data': ip_logs}
        else:
            time.sleep(3)
            get_job_instance_log(client, biz_id, job_instance_id)
    else:
        return {'result': False, 'message': res['message']}

