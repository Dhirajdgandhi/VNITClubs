from django.http import HttpResponseRedirect
from django.shortcuts import render , render_to_response
from django.core.context_processors import csrf

from django.template import RequestContext
from portalapp.models import *
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

def clubs( request ):
    args = {'page_name': ""}
    args.update ( csrf ( request ) )
    args.update ( headerdb ( request ) )

    return render_to_response ( 'VnitClubsHome.html' , args )

def clubHome(request,clubName):
     # Take pagename, find in db ,extract data and use it here.

    #Use clubName to get exact CLubName

    args = {'page_name': "",
            'clubName':clubName}
    args.update ( csrf ( request ) )
    args.update ( headerdb ( request ) )

    print clubName
    return render_to_response ( 'ClubHome.html' , args )
