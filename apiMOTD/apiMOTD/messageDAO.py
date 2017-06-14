# import datetime
from django.http import HttpResponse
from message import Message

def getMessage(date):
    message = None

    if date.weekday() == 0: #Monday
        message = "I Don't Like Mondays"
    elif date.weekday() == 1:#Tuesday
        message = "Ruby Tuesday"
    elif date.weekday() == 2: #Wednesday
        message = "Waiting for Wednesday"
    elif date.weekday() == 3: #Thursday
        message = "Thursday's Child "
    elif date.weekday() == 4:#Friday
        message = "Friday I'm in Love"
    elif date.weekday() == 5: #Saturday
        message = "Saturday Night's Alright for Fighting"
    elif date.weekday() == 6: #Sunday
        message = "Pleasant Valley Sunday"
    else: #default
        message = "Sorry, no message today"

    return Message(date, message)
