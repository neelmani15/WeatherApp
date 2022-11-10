import json
from django.shortcuts import render
import urllib.request
from datetime import *
from datetime import datetime as dt
# Create your views here.
def index(request):
    if request.method=='POST':
        city=request.POST['city']
        url=urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=imperial&appid=f8dea40766e5f177ac70d436857f5370').read()
        res=json.loads(url)
        dat=date.today()
        t=dt.now()
        tim=t.strftime("%H:%M:%S")
        data={
            "city":res['name'],
            "heading":res['weather'][0]['main'],
            "description":res['weather'][0]['description'],
            "icon":res['weather'][0]['icon'],
            "temp":res['main']['temp'],
            "humidity":res['main']['humidity'],
            "pressure":res['main']['pressure'],
            "windspeed":res['wind']['speed'],
            "code":res['sys']['country'],
            "date":dat,
            "time":tim
        }
        print(data)
    else:
        data={
            "city":"----",
            "heading":"----",
            "description":"----",
            "icon":"----",
            "temp":"----",
            "humidity":"----",
            "pressure":"----",
            "windspeed":"----",
            "code":"----",
            "date":"----",
            "time":"----"
        }
    return render(request,'index.html',data)
