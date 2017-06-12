import datetime

class Message(object):

    message = ''
    date = None

    def __init__(self, date, message):
        self.message = message
        self.date = date

    def getMessage(self):
        return self.message

    def getDate(self):
        return self.date
