# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import messageDAO
import datetime
import time
import json

def getTodaysMessage(request):
    today = datetime.datetime.fromtimestamp(time.time())
    return HttpResponse(json.dumps(messageDAO.getMessage(today).__dict__), content_type="application/json")

def getMessageByDate(request,dateString):
    dayToGet = datetime.datetime.fromtimestamp(float(dateString)/1000.0)
    return HttpResponse(json.dumps(messageDAO.getMessage(dayToGet).__dict__), content_type="application/json")
