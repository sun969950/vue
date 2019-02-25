# -*- coding: utf-8 -*-
import json

import requests

from conf.default import APP_ID, APP_TOKEN, BK_PAAS_HOST


def search_host():    #查询主机信息
    data = {
        "bk_app_code": APP_ID,
        "bk_app_secret": APP_TOKEN,
        'bk_username': "admin",
        "bk_biz_id": 2,
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
            },

    ]
    }
    url = BK_PAAS_HOST + "/api/c/compapi/v2/cc/search_host/"
    result = requests.post(url=url, data=json.dumps(data))
    res = json.loads(result.content)
    # print res
    if res['result']:
        data = res["data"]["info"]
        # data2 = data[0]["set"]
        lis = []
        for i in data:
            host_content = i["host"]
            biz_content = i["biz"]
            lis.append({"bk_host_name": host_content["bk_host_name"],
                        "bk_host_innerip": host_content["bk_host_innerip"],
                        "bk_os_name": host_content["bk_os_name"],
                        "bk_biz_name": biz_content[0]["bk_biz_name"],

                        })

        res = {"result": True, "data": data}
        return res
    else:
        res = {"result": False, "data": res}
search_host()