#!/usr/bin/env python
# encoding:utf-8
import commands
import requests


class InitConfig(object):
    def __init__(self):
        self.url = 'http://localhost:8088/'  # 服务器地址


class MP3(object):
    def __init__(self):
        pass

    def start(self, mp3_path):
        print 'Start : ' + mp3_path
        # status, output = commands.getstatusoutput('mplayer -volume 30 ' + mp3_path)
        # print status, output


class Api_alarm(InitConfig):
    def __init__(self):
        InitConfig.__init__(self)

    def alarmDetail(self):
        r = requests.get(self.url + "alarm_api.html")
        return r.json()

    def getMp3Path(self):
        r = requests.get(self.url + "mp3_api.html")
        return r.json()

    def updateMp3Path(self, ids):
        data = {
            "id": ids
        }
        r = requests.post(self.url + "mp3_api_update.html", data=data)
        print r.text


class Main(object):
    def __init__(self):
        pass

    def alarmModel(self):
        result = Api_alarm().alarmDetail()
        print result
        for r in result:
            mp3_url = result.get(r)['mp3']
            MP3().start(mp3_url)

    def mp3Model(self):
        result = Api_alarm().getMp3Path()
        for r in result:
            ids = result.get(r)['id']
            mp3_url = result.get(r)['mp3_path']
            Api_alarm().updateMp3Path(ids)
            MP3().start(mp3_url)


if __name__ == '__main__':
    Main().mp3Model()
    Main().alarmModel()
