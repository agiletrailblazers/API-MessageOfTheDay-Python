# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import messageDAO
import datetime

def messages(request):
    today = datetime.date.today()
    return HttpResponse(messageDAO.getMessage(today).getMessage())
