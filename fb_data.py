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
    return m.strftime('%HH')
def to_date(time):
    m = dateutil.parser.parse(time)
    return m.strftime('%dd')

# fb token
token = 'EAACEdEose0cBACzj6W5X7pYb839f8QtMlVwu5021lIbtFIb8TWMGrX398JrprUd8voN9zYoBpFYT0APxkFgrAFZB8LqgutIXCJ3BfumVKoMhIGIogXySgLIhjlzqgX2EZAuGhXr0D4wZAl7IDdmxWbbeBeK9DYf3fioZCfIJDntR4Y8KgSJqBx6SKZBoCA6Nyf5xZAT9j6rPBnvZC7f27WQ'
#making HTTP request to graph API
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
    print event.heading + " loading..."
    event.description = data['description']
    event.place = data['place']['name']

    #event.date = to_date(data['start_time'])
    #event.time =to_date(data['start_time'])
    event.save()

    cer = ClubEventRelationship()
    cerclub = Club.objects.get(pk=1)
    cer.club = cerclub
    print cerclub

    cerevent = event
    print cerevent
    cer.event = cerevent
    cer.save()
    print "DONE"

print "complete"