from .MainDataToICS import MainDataToICS
from .WebJWC import WebJWC
import time
import os
from hashlib import md5
import random
import json

def getData(id,password):
    web = WebJWC(id,password)
    print('TOPO1')
    web.runDriver()
    time.sleep(1)
    print('TOPO2')
    web.loginIn()
    time.sleep(1)
    print('TOPO3')
    web.getBody()
    time.sleep(1)
    print('TOPO4')
    web.dataInBs4()
    print('TOPO4')
    web.close()

def makeIcs(id,year,month,day):
    test = MainDataToICS(id,year,month,day)
    log = test.makeIcs()
    data = ''
    for i in log:
        for k,v in i.items():
            data += '%s:%s \n'%(k,v)
        data+='\n'
    data = '导入失败数：%d\n'%len(log)+'请手动导入以下课程:\n%s'%data
    return data

def makeApi(id):
    with open('./CQUClassICS/res/jsonData/user.json','r',encoding='utf-8') as fp:
        SQ = json.load(fp)
        fp.close()
    if id not in SQ[0].keys():
        SQ[0][id]=str(random.randint(1,1<<16))
        with open('./CQUClassICS/res/jsonData/user.json','w',encoding='utf-8') as fp:
            json.dump(SQ,fp,ensure_ascii=False)
            fp.close()
    with open('./CQUClassICS/res/icsData/%s.ics'%id,'rb') as fp:
        data = fp.read()
        md5v = md5()
        md5v.update((id+SQ[0][id]).encode('utf8'))
        ids = md5v.hexdigest()
        open('./CQUClassICS/res/api/%s.ics'%ids,'wb').write(data)
        return ids

def test():
    print(os.path.abspath('Event.py'))
    print(os.path.abspath(''))