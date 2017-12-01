django_project_home = "C:\stupo\VNITClubs\studentportal"

import sys,os

sys.path.append(django_project_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'studentportal.settings'
print "bfr import models"
from clubsapp.models import *
from datetime import datetime
from django.http import HttpResponseRedirect
import requests
import urllib2
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

# fb token
token = 'EAACEdEose0cBAGg48RVWh1xX07GfZCIsevZCRMi2eDRZBy2gtZBpDA6W7r4LPsRecHuX3Y4z8Db3V9p4gDZBL62os5aiH894ZBZB8qaRm97DAAraw44IzSus9fBeNZB459zVEtm7aSpXqg9ElBClGphuNksUpI2jqIaZBoeEokVjpK5XnuslDPZAx6p2TJ8HeY9M17488pmZAtuCrdTdeyvK3AQ'  # updating url
def fb_catch(url):

    #making req to fb
    jsondata = urllib2.urlopen(url)
    #convert to python data
    pydata = json.load(jsondata)
    print pydata
    return pydata

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
    event.heading = data['name']
    event.description = data['description']
    event.place = data['place']['name']

    event.date = to_date(data['start_time'])
    event.time =to_date(data['start_time'])

    cer = ClubEventRelationship()
    cerclub = Club.object.get(pk=1)
    print cerclub
    cer.club = cerclub
    cerevent = event
    print cerevent
    cer.event = cerevent
    cer.save()
    event.save()
