# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from message import Message
import datetime


class MessageTestCase(TestCase):
    def test_getMessage(self):
        dateToGet = datetime.datetime(2017, 06, 26)
        messageToEnter = "My test message"

        messageToTest = Message(dateToGet,messageToEnter)

        self.assertEqual(messageToTest.getMessage(), messageToEnter)
        self.assertEqual(messageToTest.getEpochTime(), int((dateToGet - (datetime.datetime.utcfromtimestamp(0))).total_seconds() * 1000))
