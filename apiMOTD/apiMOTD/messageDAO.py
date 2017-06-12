# import datetime
from django.http import HttpResponse
from message import Message

def getMessage(date):
    message = None

    if date.weekday() == 0:
        message = "I Don't Like Mondays"
    elif date.weekday() == 1:
        message = "Ruby Tuesday"
    elif date.weekday() == 2:
        message = "Waiting for Wednesday"
    elif date.weekday() == 3:
        message = "Thursday's Child "
    elif date.weekday() == 4:
        message = "Friday I'm in Love"
    elif date.weekday() == 5:
        message = "Saturday Night's Alright for Fighting"
    elif date.weekday() == 6:
        message = "Pleasant Valley Sunday"
    else:
        message = "Sorry, no message today"

    return Message(date, message)
