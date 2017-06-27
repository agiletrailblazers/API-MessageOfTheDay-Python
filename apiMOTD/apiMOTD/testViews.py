# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from rest_framework.test import APIClient
import datetime
import json

class ViewsTestCase(TestCase):
    def test_messageToday(self):
        client = APIClient()
        response = client.get('/motd/messages')
        self.assertTrue("message" in str(response))

        expectedString = str(int((datetime.datetime.now() - (datetime.datetime.utcfromtimestamp(0))).total_seconds() * 1000))
        self.assertTrue(expectedString in str(response))

    def test_messageMonday(self):
        dateToGet = datetime.datetime(2017, 06, 26)
        client = APIClient()
        response = client.get('/motd/messages/' + str(int((dateToGet - (datetime.datetime.utcfromtimestamp(0))).total_seconds() * 1000)))

        self.assertTrue("I Don't Like Mondays" in str(response))
