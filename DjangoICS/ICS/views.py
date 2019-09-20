from django.shortcuts import render
from django.http import HttpResponse, FileResponse
import CQUClassICS.src.MainICS as ma
import re
import os


# Create your views here.

def index(request):
    return render(request, 'ICS/index.html',{"lists":range(1,12)})


def get(request):
    usr = request.POST['username']
    pas = request.POST['password']
    data = request.POST['data']
    data = re.findall('\d+', data)
    ma.getData(usr, pas)
    log = ma.makeIcs(usr, int(data[0]), int(data[1]), int(data[2]))
    ips = ma.makeApi(usr);
    return render(request, 'ICS/get.html', {'logs': log,'api':'/ICS/api/%s.ics'%ips,'http':'www.seeknows.cn'})


def download(request):
    usr = request.POST['usr']
    fp = open('./CQUClassICS/res/icsData/%s.ics' % usr, 'rb')
    res = FileResponse(fp)
    res['Content-Type'] = 'application/octet-stream'
    res['Content-Disposition'] = 'attachment;filename="%s.ics"' % usr
    return res


def api(request, id):
    try:
        usr = id
        fp = open('./CQUClassICS/res/api/%s' % usr, 'rb')
        res = FileResponse(fp)
        res['Content-Type'] = 'application/octet-stream'
        res['Content-Disposition'] = 'attachment;filename="%s"' % usr
    except:
        return HttpResponse('Error')
    return res
