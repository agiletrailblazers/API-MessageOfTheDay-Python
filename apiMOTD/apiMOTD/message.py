import datetime
import time

class Message(object):

    message = ''
    date = None

    def __init__(self, date, message):
        self.message = message
        self.date = int((date - (datetime.datetime.utcfromtimestamp(0))).total_seconds() * 1000)

    def getMessage(self):
        return self.message

    def getDate(self):
        return self.date
