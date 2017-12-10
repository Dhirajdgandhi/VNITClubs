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



def clubHome(request,clubName):
     # Take pagename, find in db ,extract data and use it here.

    #Use clubName to get exact CLubName
    club_data = Club.objects.get(id=clubName)

    args = {'page_name': "",
            'club_data':club_data}
    args.update ( csrf ( request ) )
    args.update ( headerdb ( request ) )

    '''
    args.update({'data': data['data']})
    '''
    activity_club = ClubActivityRelationship.objects.filter(club=club_data)
    #activity_data = Activity.objects.filter(activity_club.activity)
    args.update({'activity_data': activity_club})

    return render_to_response ( 'ClubHome.html', args )

