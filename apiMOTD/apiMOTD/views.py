# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
import messageDAO
import datetime
import json

def getTodaysMessage(request):
    today = datetime.date.today()
    return JsonResponse(messageDAO.getMessage(today).__dict__)

def getMessageByDate(request,dateString):
    print dateString
    dayToGet = datetime.datetime.fromtimestamp(float(dateString)/1000.0)
    return JsonResponse(messageDAO.getMessage(dayToGet).__dict__)
