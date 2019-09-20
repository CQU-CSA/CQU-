import datetime

class Day:

    def __init__(self,year,month,day):
        '''
        设置校历，第一周星期一日期
        :param year:
        :param month:
        :param day:
        '''
        self.oneYear = year
        self.oneMonth = month
        self.oneDay = day
        self.year = year
        self.month = month
        self.day = day

    def makeCal(self):
        SevenDay = ['一', '二', '三', '四', '五', '六', '日']
        self.calDays = {}
        for weeks in range(1, 50):
            we = {}
            for week in SevenDay:
                we[week]=self.getDay()
                self.nextDay()
            self.calDays[weeks]=we

    def getDay(self):
        return {
            'year':self.year,
            'month':self.month,
            'day':self.day
        }

    def nextDay(self):
        if self.month == 2:
            if self.year % 4 == 0 and self.year % 100 != 0 or self.year % 400 == 0:
                if self.day == 29:
                    self.month += 1
                    self.day = 1
                else:
                    self.day +=1
            else:
                if self.day == 28:
                    self.month += 1
                    self.day = 1
                else:
                    self.day +=1
        elif self.month in [1,3,5,7,8,10,12]:
            if self.day == 31:
                if self.month == 12:
                    self.year += 1
                    self.month = 1
                    self.day = 1
                else:
                    self.month += 1
                    self.day = 1
            else:
                self.day += 1
        else:
            if self.day == 30:
                self.month += 1
                self.day = 1;
            else:
                self.day += 1

    def getIndex(self,data):
        self.clock = [
            {
                '1': [
                    datetime.datetime(year=data['year'], month=data['month'], day=data['day'], hour=8, minute=0, second=0),
                    datetime.datetime(year=data['year'], month=data['month'], day=data['day'], hour=8, minute=45, second=0)
                ],
                '2': [
                    datetime.datetime(year=data['year'], month=data['month'], day=data['day'], hour=8, minute=55, second=0),
                    datetime.datetime(year=data['year'], month=data['month'], day=data['day'], hour=9, minute=40, second=0)
                ],
                '3': [
                    datetime.datetime(year=data['year'], month=data['month'], day=data['day'], hour=10, minute=10, second=0),
                    datetime.datetime(year=data['year'], month=data['month'], day=data['day'], hour=10, minute=55, second=0)
                ],
                '4': [
                    datetime.datetime(year=data['year'], month=data['month'], day=data['day'], hour=11, minute=5, second=0),
                    datetime.datetime(year=data['year'], month=data['month'], day=data['day'], hour=11, minute=50, second=0)
                ],
                '5': [
                    datetime.datetime(year=data['year'], month=data['month'], day=data['day'], hour=14, minute=30, second=0),
                    datetime.datetime(year=data['year'], month=data['month'], day=data['day'], hour=15, minute=15, second=0)
                ],
                '6': [
                    datetime.datetime(year=data['year'], month=data['month'], day=data['day'], hour=15, minute=25, second=0),
                    datetime.datetime(year=data['year'], month=data['month'], day=data['day'], hour=16, minute=10, second=0)
                ],
                '7': [
                    datetime.datetime(year=data['year'], month=data['month'], day=data['day'], hour=16, minute=40, second=0),
                    datetime.datetime(year=data['year'], month=data['month'], day=data['day'], hour=17, minute=25, second=0)
                ],
                '8': [
                    datetime.datetime(year=data['year'], month=data['month'], day=data['day'], hour=17, minute=35, second=0),
                    datetime.datetime(year=data['year'], month=data['month'], day=data['day'], hour=18, minute=20, second=0)
                ],
                '9': [
                    datetime.datetime(year=data['year'], month=data['month'], day=data['day'], hour=19, minute=30, second=0),
                    datetime.datetime(year=data['year'], month=data['month'], day=data['day'], hour=20, minute=15, second=0)
                ],
                '10': [
                    datetime.datetime(year=data['year'], month=data['month'], day=data['day'], hour=20, minute=25, second=0),
                    datetime.datetime(year=data['year'], month=data['month'], day=data['day'], hour=21, minute=10, second=0)
                ],
                '11': [
                    datetime.datetime(year=data['year'], month=data['month'], day=data['day'], hour=21, minute=20, second=0),
                    datetime.datetime(year=data['year'], month=data['month'], day=data['day'], hour=22, minute=5, second=0)
                ],
                '12': [
                    datetime.datetime(year=data['year'], month=data['month'], day=data['day'], hour=22, minute=15,
                                      second=0),
                    datetime.datetime(year=data['year'], month=data['month'], day=data['day'], hour=23, minute=0,
                                      second=0)
                ],
            },
            {
                '1': [
                    datetime.datetime(year=data['year'], month=data['month'], day=data['day'], hour=8, minute=30, second=0),
                    datetime.datetime(year=data['year'], month=data['month'], day=data['day'], hour=9, minute=15, second=0)
                ],
                '2': [
                    datetime.datetime(year=data['year'], month=data['month'], day=data['day'], hour=9, minute=25, second=0),
                    datetime.datetime(year=data['year'], month=data['month'], day=data['day'], hour=10, minute=10, second=0)
                ],
                '3': [
                    datetime.datetime(year=data['year'], month=data['month'], day=data['day'], hour=10, minute=30, second=0),
                    datetime.datetime(year=data['year'], month=data['month'], day=data['day'], hour=11, minute=15, second=0)
                ],
                '4': [
                    datetime.datetime(year=data['year'], month=data['month'], day=data['day'], hour=11, minute=25, second=0),
                    datetime.datetime(year=data['year'], month=data['month'], day=data['day'], hour=12, minute=10, second=0)
                ],
                '5': [
                    datetime.datetime(year=data['year'], month=data['month'], day=data['day'], hour=14, minute=00, second=0),
                    datetime.datetime(year=data['year'], month=data['month'], day=data['day'], hour=14, minute=45, second=0)
                ],
                '6': [
                    datetime.datetime(year=data['year'], month=data['month'], day=data['day'], hour=14, minute=55, second=0),
                    datetime.datetime(year=data['year'], month=data['month'], day=data['day'], hour=15, minute=40, second=0)
                ],
                '7': [
                    datetime.datetime(year=data['year'], month=data['month'], day=data['day'], hour=16, minute=00, second=0),
                    datetime.datetime(year=data['year'], month=data['month'], day=data['day'], hour=16, minute=45, second=0)
                ],
                '8': [
                    datetime.datetime(year=data['year'], month=data['month'], day=data['day'], hour=16, minute=55, second=0),
                    datetime.datetime(year=data['year'], month=data['month'], day=data['day'], hour=17, minute=40, second=0)
                ],
                '9': [
                    datetime.datetime(year=data['year'], month=data['month'], day=data['day'], hour=19, minute=00, second=0),
                    datetime.datetime(year=data['year'], month=data['month'], day=data['day'], hour=19, minute=45, second=0)
                ],
                '10': [
                    datetime.datetime(year=data['year'], month=data['month'], day=data['day'], hour=19, minute=55, second=0),
                    datetime.datetime(year=data['year'], month=data['month'], day=data['day'], hour=20, minute=40, second=0)
                ],
                '11': [
                    datetime.datetime(year=data['year'], month=data['month'], day=data['day'], hour=20, minute=50, second=0),
                    datetime.datetime(year=data['year'], month=data['month'], day=data['day'], hour=21, minute=35, second=0)
                ],
                '12': [
                    datetime.datetime(year=data['year'], month=data['month'], day=data['day'], hour=21, minute=45,
                                      second=0),
                    datetime.datetime(year=data['year'], month=data['month'], day=data['day'], hour=21, minute=30,
                                      second=0)
                ]
            }
        ]
        return self.clock

    def getCalDays(self):
        return self.calDays

