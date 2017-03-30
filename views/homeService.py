#!/usr/bin/env python
# encoding:utf-8
from db.DBHelper import DBMysql
from sqlalchemy.orm import sessionmaker
from model.mp3Model import Mp3Model
from model.mp3MQModel import Mp3MqModel
from model.alarmModel import AlarmModel
from util.utilDate import getDateTime
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

DBSession = sessionmaker(bind=DBMysql().getEngine())


def queryMp3():
    session = DBSession()
    try:
        result = session.query(Mp3Model).all()
        return result
    except Exception, e:
        print e
    finally:
        session.close()


def addMp3(name, gs, url, m):
    session = DBSession()
    try:
        new_mp3model = Mp3Model(
            mp3_path=url,
            mp3_name=name,
            mp3_name1=m,
            mp3_author=gs,
            create_time=getDateTime()
        )
        session.add(new_mp3model)
        session.commit()
    except Exception, e:
        print e
        session.rollback()
    finally:
        session.close()


def addMp3bf(url):
    session = DBSession()
    try:
        new_mp3model = Mp3MqModel(
            mp3_path=url,
            type=0
        )
        session.add(new_mp3model)
        session.commit()
    except Exception, e:
        print e
        session.rollback()
    finally:
        session.close()


def queryMp3Mq():
    session = DBSession()
    try:
        result = session.query(Mp3MqModel).filter(Mp3MqModel.type == 0).all()
        return result
    except Exception, e:
        print e
    finally:
        session.close()


def Mp3MqUpdate(id):
    session = DBSession()
    try:
        session.query(Mp3MqModel).filter(Mp3MqModel.id == id).update({'type': str(1)})
        session.commit()
    except Exception, e:
        print e
    finally:
        session.close()


def queryAlarm():
    session = DBSession()
    try:
        result = session.query(AlarmModel).all()
        return result
    except Exception, e:
        print e
    finally:
        session.close()


def addAlarm(times, mp3path):
    session = DBSession()
    try:
        new_AlarmModel = AlarmModel(
            time=times,
            path=mp3path,
            create_time=getDateTime()
        )
        session.add(new_AlarmModel)
        session.commit()
    except Exception, e:
        print e
        session.rollback()
    finally:
        session.close()


def delAlarm(id):
    session = DBSession()
    try:
        session.query(AlarmModel).filter(AlarmModel.id == id).delete()
        session.commit()
    except Exception, e:
        print e
    session.close()
