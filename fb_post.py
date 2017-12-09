django_project_home = "C:\stupo\VNITClubs\studentportal"

import sys,os

sys.path.append(django_project_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'studentportal.settings'
print "bfr import models"
from clubsapp.models import *
from datetime import datetime
from django.http import HttpResponseRedirect
import requests
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

print "1"
#for generate random string
def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

#retrive image from the URL
def img_download(url):
    name = randomword(10)
    img_name = name + '.jpg'
    #return urllib.urlretrieve(url, img_name)
print"2"
# fb token
token = 'EAACEdEose0cBABNMqjnnBbUrlS4OZAVIwVxzfuL9tVUURLzvQoDYZCECdufIQAI1kAmDSfSuDv5xdKg7t4sBJ5xpoqYkkMhZANmguFkDPrGqPB0bYqokbncYSyqaU6Fvgdxd2xkSYFsxgk7G4hmBo2p9jmIyXHFWCgPTvagHkFU9ZAZBfexWs3LBMKXIeAJB1wVOleTvI5mLlSsEi9jWO'
#making HTTP request to graph API
def fb_catch(url):

    #making req to fb
    jsondata = urllib2.urlopen(url)
    #convert to python data
    pydata = json.load(jsondata)
    print pydata
    return pydata
print"3"
'''
clubs = Club()
fbids = clubs.fb_id
for fbid in fbids:
'''


fbid = '125409010890443' #mag
#fbid = '1413870692209917' #ecell
#fbid = '' #ieee
#fbid = '122188297874827' #prayaas
#fbid = '558880000805766' #astro
#fbid = '' #ivlabs
#fbid = '174942216314910' #tesla
#fbid = '' #grooves
#fbid = '190530800978437' #iridecence
#fbid = '302597396486782'#team v
#fbid = '' #iiche



# url for getting events
posturl = 'https://graph.facebook.com/v2.11/' + fbid + '/posts?fields=full_picture,message,created_time&limit=8&access_token='+token

postdata = fb_catch(posturl)
postdata= postdata['data']

for data in postdata:
    activity = Activity()
    activity.title = fbid
    activity.date = to_date(data['created_time'])
    activity.description = data['message']
    activity.save()

    car = ClubActivityRelationship()
    carclub = Club.objects.get(pk=1)
    car.club = carclub
    print carclub
    caractivity = activity
    print caractivity
    car.activity = caractivity
    car.save()


    photo = Photos()
    photograph_url = data['full_picture'] #url
    #write a code to get image from url and save it into db
    #example :  https://stackoverflow.com/questions/16174022/download-a-remote-image-and-save-it-to-a-django-model

    photo.photograph = img_download(photograph_url)
    photo.details = data['message']
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


