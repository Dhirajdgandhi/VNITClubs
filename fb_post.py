django_project_home = "C:\stupo\VNITClubs\studentportal"

import sys,os

sys.path.append(django_project_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'studentportal.settings'
print "bfr import models"
from clubsapp.models import *
from datetime import datetime
from django.http import HttpResponseRedirect
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
import requests
from urlparse import urlparse
import urllib2, urllib
import random, string
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

#for generate random string
def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

# fb token
token = 'EAACEdEose0cBACl83wqGf1Rn9U3dh2ZBR5FIfMS5pMFTP2mhKRcyGIexbkGF7f3PE1IzzGoSzfZBUyMVZCqZCi2jfaGrL81ZBdn10qL0pbqy2sRdGZCztNMZCe1997MzB5U4S6TGVeoQiCuMikgmbnoy5hsQmmyEgnmRTZC3EL52oF2H7IaDFp9UrY0xbtwbnXM82CF1aZBXfdAZDZD'
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
posturl = 'https://graph.facebook.com/v2.11/' + fbid + '/posts?fields=full_picture,message,created_time&limit=8&access_token='+token

postdata = fb_catch(posturl)
postdata= postdata['data']

for data in postdata:
    activity = Activity()
    activity.title = fbid
    activity.date = to_date(data['created_time'])
    try:
        activity.description = data['message']
    except KeyError:
        continue

    try:
        activity.save()
    except:
        continue


    car = ClubActivityRelationship()
    carclub = Club.objects.get(pk=12)
    car.club = carclub
    print carclub
    caractivity = activity
    print caractivity
    car.activity = caractivity
    car.save()

    print "downloading.. photo"
    photo = Photos()

    try:
        url = data['full_picture'] #url
        #assigning name to image
        img_name = carclub.shortName+ "_act"  + "_" + randomword(4) + ".jpg"
        #creating a temporary file
        img_temp = NamedTemporaryFile()
        #making request, reading and writing into empty temp file
        img_temp.write(urllib2.urlopen(url).read())
        img_temp.flush()
        #save the photo
        photo.photograph.save(img_name, File(img_temp))
        print "Downloaded and saved ;>"
    except KeyError:
        continue

    try:
        photo.details = data['message']
    except KeyError:
        continue
    photo.dateOfCapture = to_date(data['created_time'])
    photo.save()

    apr = ActivityPhotoRelationship()
    apractivity = Activity.objects.get(pk=activity.id)
    apr.activity = apractivity
    print apractivity
    apr.photo = Photos.objects.get(pk=photo.id)
    apr.save()

    print("DONE")
print("Complete")


