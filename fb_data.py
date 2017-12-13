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
    return m.strftime('%H:%M:%S')
def to_date(time):
    m = dateutil.parser.parse(time)
    return m.strftime('%Y-%m-%d')

# fb token
token = 'EAACEdEose0cBAHRnPj08sWSAVb43mmHprzK6iCkyZAKZBbAPX8MmEvNdr53KTVYvYOZAPKsMl15S8NAfiuCQvZBGqr9UmwgbE4PIG7DcrO7mrGEr6ySNunRpT3RYWFveqwf3KpJRfKJQCpHaRiuZCVUbOPpUEV83o1M8Uf1G4qRFZAQWILpPna0eU9g8qzABQeu7ZCtVTGN5DU4kTTYF6av'
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


#fbid = '125409010890443' #mag
#fbid = '1413870692209917' #ecell
#fbid = '' #ieee
#fbid = '122188297874827' #prayaas
#fbid = '558880000805766' #astro
#fbid = '1641158256150398' #ivlabs
#fbid = '174942216314910' #tesla
#fbid = '' #grooves
#fbid = '190530800978437' #iridecence
#fbid = '302597396486782'#team v
#fbid = '1492529371023579' #iiche
#fbid = '109896629705563' #hallabol


# url for getting events
eventurl = 'https://graph.facebook.com/v2.11/' + fbid + '/events?limit=6&access_token='+token

eventdata = fb_catch(eventurl)
eventdata = eventdata['data']

for data in eventdata:
    event = Event()
    event.heading = data['name']
    print event.heading + " loading..."
    event.description = data['description']
    event.place = data['place']['name']

    event.date = to_date(data['start_time'])
    event.time = to_time(data['start_time'])
    event.save()

    cer = ClubEventRelationship()
    cerclub = Club.objects.get(pk=11)
    cer.club = cerclub
    print cerclub

    cerevent = event
    print cerevent
    cer.event = cerevent
    cer.save()
    print "DONE"

print "complete"