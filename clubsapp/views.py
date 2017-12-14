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
    activity_club = ClubActivityRelationship.objects.filter(club=club_data)[:4]
    args.update({'activity_data': activity_club})

    event_club =  ClubEventRelationship.objects.filter(club = club_data)[:4]
    args.update({'event_data': event_club})

    club_gall = ClubPhotoRelationship.objects.filter(club = club_data)[:8]
    args.update({'gall_data': club_gall})

    return render_to_response ( 'ClubHome.html', args )

