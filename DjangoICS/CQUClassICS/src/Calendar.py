from .Event import Event

class Calendar:
    '''
    日历对象
    '''
    def __init__(self,calendarId = '91020000'):
        '''
        新建日历
        :param calendarId:日历名称
        '''
        self.events = {}
        self.eventLength = 0
        self.calendarId = calendarId

    def addEvent(self,**kwargs):
        '''
        添加事件
        :param kwargs:事件信息
            SUMMARY: 事件名
            DTSTART: 事件开始时间
            DTEND: 时间结束时间
            DESCRIPTION: 备注
            LOCATION: 时间地点
            DTSTAMP: 创建时间
        :return: 事件id
        '''
        event = Event(kwargs)
        eventId = self.eventLength
        self.events[eventId] = event
        self.eventLength += 1
        return eventId

    def removeEvent(self,eventId):
        '''
        删除事件
        :param eventId:
        :return:
        '''
        self.events.pop(eventId)

    def modifyEvent(self,eventId,**kwargs):
        '''
        修改事件
        :param eventId: 被修改事件id
        :param kwargs: 修改内容
        :return:
        '''
        for myKey,myValue in kwargs.items():
            self.events[eventId].eventData[myKey] = myValue

    def getICSText(self):
        '''
        返回ICS格式文本
        :return: string
        '''
        self.calendarText = """BEGIN:VCALENDAR\nPRODID:-//Google Inc//Google Calendar 70.9054//EN\nVERSION:2.0\nCALSCALE:GREGORIAN\nMETHOD:PUBLISH\nX-WR-CALNAME:CQU课表%s\nX-WR-TIMEZONE:Asia/Chongqing\n""" % self.calendarId
        for myKey,myValue in self.events.items():
            self.calendarText += myValue.toString()
        self.calendarText += "END:VCALENDAR"
        return self.calendarText

    def saveAsICSFile(self):
        '''
        保存到文件
        :return:
        '''
        icsText = self.getICSText()
        open('./CQUClassICS/res/icsData/%s.ics'%self.calendarId,"w",encoding='utf8').write(icsText)