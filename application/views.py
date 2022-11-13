import datetime, time

from django.shortcuts import render,HttpResponse

# Create your views here.
from django.utils.timezone import utc

from application.models import opensnz


def dash(request):
    one_day_ago = datetime.datetime.now() - datetime.timedelta(days=1)
    labels = []
    dataa = []
    all = opensnz.objects.all()
    print("all", all)
    for i in all:
        labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
        print("labels", labels)
        dataa.append(i.temp)
    lst = opensnz.objects.last()
    context={'all':all,'lst':lst,'labels':labels,'dataa':dataa}
    return render(request,"acc.html",context)

def dash2(request):
    # one_day_ago = datetime.datetime.now() - datetime.timedelta(days=1)
    labels = []
    dataa = []
    # posts = opensnz.objects.filter(dt__gte=one_day_ago)
    # print(posts)
    # for i in posts:
    #     labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
    #     dataa.append(i.temp)
    #
    all = opensnz.objects.all()
    # print("all",all)
    for i in all:
        labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
        # print("labels", labels)
        # dataa.append(i.temp)
        # x=i.dt
        #
        # for_js = int(time.mktime(x.timetuple())) * 1000
        # print("for_js",for_js)
        #
        # labels.append(for_js.strftime("%M %d %Y %H:%M:%S"))
        # lst = opensnz.objects.last()
    context={'all':all,'labels':labels,'dataa':dataa}
    return render(request,"line.html",context)