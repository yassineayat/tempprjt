import datetime

from django.shortcuts import render,HttpResponse

# Create your views here.
from application.models import opensnz


def dash(request):
    one_day_ago = datetime.datetime.now() - datetime.timedelta(days=1)
    labels = []
    dataa = []
    posts = opensnz.objects.filter(dt__gte=one_day_ago)
    print(posts)
    for i in posts:
        labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
        dataa.append(i.temp)

    all = opensnz.objects.all()
    lst = opensnz.objects.last()
    context={'all':all,'lst':lst,'labels':labels,'dataa':dataa}
    return render(request,"acc.html",context)