from .MainCalendarEvent import MainCalendarEvent
from .Day import Day
import json
import re

class MainDataToICS:

    def __init__(self,stuId,year,month,day):
        self.stuId = stuId
        self.year=year
        self.month=month
        self.day=day
        self.log = []
        self.error = []
        self.classNumber = {}

    def makeIcs(self):
        with open('./CQUClassICS/res/jsonData/%s.json'%self.stuId,'r',encoding='utf-8') as fp:
            self.data = json.load(fp)
            fp.close()
        self.mainCalendarEvent = MainCalendarEvent(self.stuId)
        self.dayTime = Day(self.year, self.month, self.day)
        self.dayTime.makeCal()
        self.calDay = self.dayTime.getCalDays()
        for oneClassData in self.data:
            try:
                weekData = oneClassData['周次']
                dayData = oneClassData['节次']
                weekNumber = []
                weekDay = dayData[0]
                dayNumber = re.findall(r'\d+',dayData)
                DESCRIPTION = ''
                school = oneClassData['地点'][0]
                if(school == "D"):
                    school=-1
                else:
                    school=0

                for k,v in oneClassData.items():
                    DESCRIPTION += "%s:%s;"%(k,v)


                if len(weekData) < 3:
                    weekNumber.append(int(weekData))
                else:
                    weekData = weekData.split(',')
                    for A_B in weekData:
                        if len(A_B) < 3:
                            weekNumber.append(int(A_B))
                        else:
                            A_B = A_B.split('-')
                            weekNumber+=range(int(A_B[0]),int(A_B[1])+1)


                for weekN in weekNumber:
                    self.clock = self.dayTime.getIndex(self.calDay[weekN][weekDay])
                    if oneClassData['课程'] not in self.classNumber.keys():
                        self.classNumber[oneClassData['课程']] = 0
                    else:
                        self.classNumber[oneClassData['课程']] += 1

                    self.mainCalendarEvent.addEvent(
                        SUMMARY=oneClassData['课程'],
                        DTSTART=self.clock[school][dayNumber[0]][0],
                        DTEND=self.clock[school][dayNumber[-1]][1],
                        DESCRIPTION=DESCRIPTION,
                        LOCATION=oneClassData['地点'],
                        UID=str(self.stuId)+oneClassData['课程']+str(self.classNumber[oneClassData['课程']])#同一id
                    )
            except Exception:
                self.log.append(oneClassData)
        self.mainCalendarEvent.getCalendar().saveAsICSFile()
        open('./CQUClassICS/res/log/%s.json'%self.stuId,'w',encoding='utf8').write(str(self.log))
        return self.log


