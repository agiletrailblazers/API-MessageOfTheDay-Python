# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
import messageDAO
import datetime


class MessageDAOTestCase(TestCase):
    def test_messageMonday(self):
        dateToGet = datetime.datetime(2017, 06, 26)
        self.assertEqual(messageDAO.getMessage(
            dateToGet).getMessage(), "I Don't Like Mondays")

    def test_messageTuesday(self):
        dateToGet = datetime.datetime(2017, 06, 27)
        self.assertEqual(messageDAO.getMessage(
            dateToGet).getMessage(), "Ruby Tuesday")

    def test_messageWednesday(self):
        dateToGet = datetime.datetime(2017, 06, 28)
        self.assertEqual(messageDAO.getMessage(
            dateToGet).getMessage(), "Waiting for Wednesday")

    def test_messageThursday(self):
        dateToGet = datetime.datetime(2017, 06, 29)
        self.assertEqual(messageDAO.getMessage(
            dateToGet).getMessage(), "Thursday's Child")

    def test_messageFriday(self):
        dateToGet = datetime.datetime(2017, 06, 30)
        self.assertEqual(messageDAO.getMessage(
            dateToGet).getMessage(), "Friday I'm in Love")

    def test_messageSaturday(self):
        dateToGet = datetime.datetime(2017, 07, 1)
        self.assertEqual(messageDAO.getMessage(
            dateToGet).getMessage(), "Saturday Night's Alright for Fighting")

    def test_messageSunday(self):
        dateToGet = datetime.datetime(2017, 07, 2)
        self.assertEqual(messageDAO.getMessage(
            dateToGet).getMessage(), "Pleasant Valley Sunday")
