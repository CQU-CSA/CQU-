import time
from selenium import webdriver
from bs4 import BeautifulSoup
import json

class WebJWC:

    def __init__(self,studentId,password):
        self.urlJWC = 'http://202.202.1.176:8080'
        self.studentId = studentId
        self.password = password
        self.chromePath = './CQUClassICS/res/chromedriver'
        self.data = []

    def runDriver(self):
        self.driver = webdriver.Chrome(self.chromePath)
        self.driver.get(self.urlJWC)

    def loginIn(self):
        self.driver.switch_to_frame('frmLogin')
        usernameInput = self.driver.find_element_by_id('txt_dsdsdsdjkjkjc')
        passwordInput = self.driver.find_element_by_id('txt_dsdfdfgfouyy')
        button = self.driver.find_element_by_class_name('but20')
        usernameInput.clear()
        usernameInput.send_keys(self.studentId)
        passwordInput.clear()
        passwordInput.send_keys(self.password)
        button.click()

    def dataInBs4(self):
        elements = open('./CQUClassICS/res/htmlData/body.html','r',encoding='utf8').read()
        soup = BeautifulSoup(elements,'html.parser')
        text = soup.prettify()
        open('./CQUClassICS/res/htmlData/body.html','w',encoding='utf8').write(text)
        tab = soup.find_all(name='table',attrs={'class':'page_table'})
        for i in range(len(tab)):
            if(i%2==0):
                continue
            index = []
            for td in tab[i].thead.tr.find_all('td'):
                index.append(td.text.replace(' ','').replace('\n','').strip())
            index[-1]='节次'
            index[-2]='周次'
            index.append('地点')
            for tr in tab[i].tbody.find_all('tr'):
                data = {}
                tds = tr.find_all('td')
                for j in range(len(tds)):
                    data[index[j]]=tds[j].text.replace(' ','').replace('\n','').strip()
                    if(data[index[j]]=='' and index[j] in ['课程','学分','总学时','讲授学时','上机学时']):
                        data[index[j]]=self.data[-1][index[j]]
                self.data.append(data)
        #查重
        le = len(self.data)
        count = 0
        temp = []
        while count <le:
            te = self.data[count]
            te.pop('序号')
            if te not in temp:
                temp.append(te)
                count += 1
                continue
            else:
                self.data.pop(count)
                le -= 1

        with open('./CQUClassICS/res/jsonData/%s.json'%self.studentId,'w',encoding='utf8') as fp:
            json.dump(self.data,fp,ensure_ascii=False)







    def getBody(self):
        self.driver.switch_to_frame('frmbody')
        time.sleep(0.2)
        btn = self.driver.find_element_by_id('memuBarBtn3')
        btn.click()
        time.sleep(0.2)
        btn = self.driver.find_element_by_xpath('//span[@value="../znpk/Pri_StuSel.aspx"]')
        btn.click()
        time.sleep(0.2)
        self.driver.switch_to_frame('frmMain')
        time.sleep(0.2)
        btn = self.driver.find_element_by_xpath('//input[@type="button"]')
        btn.click()
        time.sleep(0.2)
        self.driver.switch_to_frame('frmRpt')
        text = self.driver.page_source
        open('./CQUClassICS/res/htmlData/body.html','w',encoding='utf8').write(text)


    def close(self):
        #curHandle = self.driver.current_window_handle  # 获取当前窗口聚丙
        allHandle = self.driver.window_handles  # 获取所有聚丙
        for h in allHandle:
            self.driver.switch_to.window(h)
            self.driver.close()



