django_project_home = "C:\stupo\VNITClubs\studentportal"

import sys,os

sys.path.append(django_project_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'studentportal.settings'
print "bfr import models"
from clubsapp.models import *
from datetime import datetime
import requests
import json
import datetime
import dateutil.parser
print "aftr"

def to_time(time):
    m = dateutil.parser.parse(time)
    return m.strftime('%HH:%mm')
def to_date(time):
    m = dateutil.parser.parse(time)
    return m.strftime('%dd/%MM/%yyyy')

def fb_catch(url):

    url = url + token
    #making req to fb
    jsondata = requests.get(url)
    #convert to python data
    pydata = jsondata.json()
    print pydata
    return pydata

# fb token
token = 'EAACEdEose0cBAKypb0HDOBsiJhE8348bij4ZCgegFRoAow1n5bWzuE83QPD6bCZBwMwbpJy3ahGZADfnVf03uV5KC4CqOMUHzhO72FgeN9n9XrvOuri4BIhZAbYB1ZCBa02ZBqZCWK15GTFYEvZA2PdgzeEDIdshsJDx3UzGWmWxpmzZAsHjuOHzM7EZCPz3RZAA8Vx0ZBu3Tto4t4D5fuU3TN2F'  # updating url
'''
clubs = Club()
fbids = clubs.fb_id
for fbid in fbids:
'''
fbid = '125409010890443'
# url for getting events
eventurl = 'https://graph.facebook.com/v2.11/' + fbid + '/events?access_token='+token

eventdata = fb_catch(eventurl)
eventdata= eventdata['data']

for data in eventdata:
    event = Event()
    event.heading = data.name
    event.description = data.description
    event.place = data.place.name

    event.date = to_date(data.start_time)
    event.time =to_date(data.start_time)

    cer = ClubEventRelationship()
    cerclub = Club.object.get(fb_id=fbid)
    print cerclub
    cer.club = cerclub
    cerevent = event
    print cerevent
    cer.event = cerevent
    cer.save()
    event.save()
