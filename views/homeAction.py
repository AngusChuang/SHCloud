#!/usr/bin/env python
# encoding:utf-8
from flask import Blueprint, render_template, abort, request, redirect, session, jsonify
import json
import homeService
import time
from util.wy163 import Mp3

homeAction = Blueprint('homeAction', __name__, template_folder='templates/')


# 仪表盘
@homeAction.route("/", methods=['GET', 'POST'])
@homeAction.route("/index.html", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pass
    else:
        return render_template("index.html")


# 灯光模块

@homeAction.route("/led.html", methods=['GET', 'POST'])
def led():
    if request.method == 'POST':
        pass
    else:
        return render_template("led.html")


# MP3模块
@homeAction.route("/mp3.html", methods=['GET', 'POST'])
def mp3():
    if request.method == 'POST':
        type = request.form.get('type')
        if type == "1":
            mp3_name = request.form.get('mp3_name')
            result = Mp3().queryList(mp3_name)
            return jsonify(result)
        elif type == "2":
            mp3_name = request.form.get('name')
            gs = request.form.get('gs')
            url = request.form.get('url')
            m = request.form.get('m')
            homeService.addMp3(mp3_name, gs, url, m)
            return 'success'
        elif type == "3":
            url = request.form.get('url')
            homeService.addMp3bf(url)
            return 'success'
    else:
        result = homeService.queryMp3()
        return render_template("mp3.html", result=result)


@homeAction.route("/mp3_api.html", methods=['GET', 'POST'])
def mp3_api():
    result = homeService.queryMp3Mq()

    rjson = {}
    i = 0
    for r in result:
        s = {}
        s['id'] = r.id
        s['mp3_path'] = r.mp3_path
        rjson[i] = s
        i = i + 1

    return jsonify(rjson)


@homeAction.route("/mp3_api_update.html", methods=['GET', 'POST'])
def mp3_api_update():
    id = request.form.get("id")
    homeService.Mp3MqUpdate(id)
    return 'success'


# 闹铃模块

@homeAction.route("/alarm.html", methods=['GET', 'POST'])
def alarm():
    if request.method == 'POST':
        types = request.form.get('types')
        if types == '1':
            id = request.form.get('id')
            homeService.delAlarm(id)
        else:
            times = request.form.get('times')
            mp3path = request.form.get('mp3path')
            homeService.addAlarm(times, mp3path)
        return 'success!'
    else:
        result = homeService.queryAlarm()
        return render_template("alarm.html", result=result)


@homeAction.route("/alarm_api.html", methods=['GET', 'POST'])
def alarm_api():
    result = homeService.queryAlarm()
    rjson = {}
    i = 0
    for r in result:
        ti1 = time.strftime('%H:%M', time.localtime(time.time()))
        print ti1
        print r.time
        if r.time == ti1:
            s = {}
            s['time'] = r.time
            s['mp3'] = r.path
            rjson[i] = s
            i = i + 1

    return jsonify(rjson)
