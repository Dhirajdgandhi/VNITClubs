import datetime
import dateutil.parser
from django import template

register = template.Library()

def to_month(time):
    m = dateutil.parser.parse(time)
    return m.strftime('%m')
register.filter('to_month',to_month)

def to_day(time):
    m = dateutil.parser.parse(time)
    return m.strftime('%d')
register.filter('to_day',to_day)

def to_time(time):
    m = dateutil.parser.parse(time)
    return m.strftime('%H:%M')
register.filter('to_time',to_time)