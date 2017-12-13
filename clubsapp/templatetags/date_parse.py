import datetime
import dateutil.parser
from django import template

register = template.Library()

def to_month(time):
    m = dateutil.parser.parse(str(time))
    return m.strftime('%m')
register.filter('to_month',to_month)

def to_day(time):
    m = dateutil.parser.parse(str(time))
    return m.strftime('%d')
register.filter('to_day',to_day)

def to_time(time):
    m = dateutil.parser.parse(str(time))
    return m.strftime('%H:%M')
register.filter('to_time',to_time)


def event_class(data):

    if data %2 == 0:
        return 'event-block-o animatable'
    else:
        return 'event-block animatable'

register.filter('event_class',event_class)