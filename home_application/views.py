# -*- coding: utf-8 -*-
from common.mymako import render_mako_context, render_json
from conf.default import LOGOUT_URL


def home(request):
    return render_mako_context(request, '/index.prod.html')


def login_info(request):
    resp = render_json({
        "result": True,
        "data": {
            "username": request.user.username,
            "logout_url": LOGOUT_URL
        }})
    from django.core.context_processors import csrf
    resp.set_cookie('cwcsrftoken', csrf(request)['csrf_token'])
    return resp


def test(request):
    print request.body
    return render_json({'result': True})