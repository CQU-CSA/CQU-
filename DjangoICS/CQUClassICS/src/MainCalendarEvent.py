import datetime
from .Calendar import Calendar
from .Event import Event

class MainCalendarEvent:

    def __init__(self,studentId):
        self.calenter = Calendar(studentId)
        self.studentId = studentId
        self.len = 0

    def addEvent(self,SUMMARY, DTSTART, DTEND, DESCRIPTION, LOCATION,UID):
        '''
        添加事件
        :param SUMMARY: 事件民
        :param DTSTART: 事件开始时间
        :param DTEND:事件结束时间
        :param DESCRIPTION: 备注
        :param LOCATION: 时间地点
        :return:
        '''

        timeFormat = "TZID=Asia/Chongqing:{date.year}{date.month:0>2d}{date.day:0>2d}T{date.hour:0>2d}{date.minute:0>2d}00"
        dtStart = timeFormat.format(date=DTSTART)
        dtEnd = timeFormat.format(date=DTEND)
        createTime = datetime.datetime.today().strftime("%Y%m%dT%H%M%SZ")
        self.calenter.addEvent(
            SUMMARY = SUMMARY,
            DTSTART = dtStart,
            DTEND = dtEnd,
            DTSTAMP = createTime,
            UID = UID,
            SEQUENCE = "0",
            CREATED = createTime,
            DESCRIPTION = DESCRIPTION,
            LAST_MODIFIED = createTime,
            LOCATION = LOCATION,
            STATUS="CONFIRMED",
            TRANSP = "OPAQUE"
        )
        self.len += 1

    def getCalendar(self):
        return self.calenter