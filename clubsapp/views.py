from django.http import HttpResponseRedirect
from django.shortcuts import render , render_to_response
from django.core.context_processors import csrf

from django.template import RequestContext
from portalapp.models import *
import requests
import json
import datetime, dateutil.parser
#
# Create your views here.
#  For trial use this
#
# def helloworld(request):
#     print "hello world"
#     user = ForLogin.objects.filter ( clg_id=15616 )
#     print user
#     return HttpResponseRedirect ( 'clubs' )
from portalapp.views import *
from clubsapp.models import *

def clubs( request ):

    clubs = Club.objects.all()
    args = {'page_name': ""}
    args.update({'clubs':clubs})
    args.update ( csrf ( request ) )
    args.update ( headerdb ( request ) )

    return render_to_response ( 'VnitClubsHome.html' , args )

def fb_catch(url):

    #fb token
    token = 'EAACEdEose0cBANxvisRgxeBHOshk3Tpw4ezEgrSXK7TcPycDVYU3ZBuBa4LePFa5lLClBX5FZCZBVixhhAACuppA0nCZCLGT3UsZCKvkjmGkPL6Efp8AxUk0lF3mKHcjiZAKyfSSok96YSxoOqxNZBZBiWOaWz7wy5IZBk9OVL652LZAhVSVXrAqMICpEnUnbZBCz5wB3J9f8uV2KbF99FN4UZCq' #updating url
    url = url + token
    #making req to fb
    jsondata = requests.get(url)
    #convert to python data
    pydata = jsondata.json()
    print pydata
    return pydata




def clubHome(request,clubName):
     # Take pagename, find in db ,extract data and use it here.

    #Use clubName to get exact CLubName
    club_data = Club.objects.get(id=clubName)

    args = {'page_name': "",
            'club_data':club_data}
    args.update ( csrf ( request ) )
    args.update ( headerdb ( request ) )

    '''
    clubfbid = '125409010890443'

    eventurl = 'https://graph.facebook.com/v2.10/'+clubfbid+'/events?access_token='
    data = fb_catch(eventurl)
    args.update({'data': data['data']})
    '''

    return render_to_response ( 'ClubHome.html', args )

'''
access_token='EAACEdEose0cBAC4Jdyi8isEwZCm7hxWJ9rfAXFbJbGRBC2EnL62E0FZBxcQqN7WqAOZBvG9D5Vp3E3ZBGPQB6cLc0lazpa71ZCaZBch9zFnbGSl2rl1HffE0mNVjpLIKaeHS1OL6iEcjxTgPeYn2g6PqQP0Y6spAsZB8SoxZCkZCcAZA3YmZAdqHO0cGR02wiLmWlbCAR1l4WQV95kHRP6uB5VH'
app_id = "1552794168112376"                       # Obtained from https://developers.facebook.com/
client_secret = "dc00b43c9493341844ee87f137821b02"         # Obtained from https://developers.facebook.com/

link = "https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id=" + app_id +"&client_secret=" + client_secret + "&fb_exchange_token=" + access_token
s = requests.Session()
token = s.get(link).content
token = token.split("&")[0]                 # this strips out the expire info (now set set about 5184000 seconds, or 60 days)
token = token.strip("access_token=")        # Strips out access token
print token
'''