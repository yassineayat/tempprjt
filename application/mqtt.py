from django.test import TestCase

# Create your tests here.
import datetime

import paho.mqtt.client as mqtt
import django
django.setup()

from application.models import *
from application.models import opensnz


def on_connect(client, userdata, flags, rc):
    #print("Connected with result code " + str(rc)) #notify about established connection
    client.subscribe("apptest")



def on_message(client, userdata, msg):
    ms = msg.payload
    data = str(ms[0: len(ms)])[2:-1]
    # data = str(ms)
    print("Your message:" + data) #display received message
    ss = data.split(' ')
    print(ss)
    opensnz.objects.create(temp=float(data))
    print("//*//*//*//")


try:
    client = mqtt.Client()
    # client.username_pw_set(username="opensnz", password="opensnz")
    client.connect("broker.hivemq.com", 1883, 60)
    client.on_connect = on_connect
    client.on_message = on_message
    client.loop_start() #do not disconnect

except Exception as e:
    print(e)
    pass
