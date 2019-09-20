class Event:
    '''
    事件对象
    :eventData:事件内容
    '''
    def __init__(self,kwargs):
        '''
        事件对象
        :param kwargs:事件内容
        '''
        self.eventData = kwargs

    def toString(self):
        '''
        事件导出为string
        :return:
        '''
        self.eventText = "BEGIN:VEVENT\n"
        for myKey,myValue in self.eventData.items():
            myKey = str(myKey).replace('_','-')
            if myKey not in ["ORGANIZER","DTSTART","DTEND"]:
                self.eventText +="%s:%s\n"%(myKey,myValue)
            else:
                self.eventText +="%s;%s\n"%(myKey,myValue)
        self.eventText += "END:VEVENT\n"
        return self.eventText