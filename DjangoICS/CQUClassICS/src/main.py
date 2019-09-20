from MainDataToICS import MainDataToICS
from  WebJWC import WebJWC
import time


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
    data = '导入失败数：%d\n'%len(log)+'请手动导入一下课程:\n%s'%data
    return data

getData('20174250','boyfriend@11526')
log = makeIcs('20174250',2019,9,2)
print(log)
