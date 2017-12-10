from django.http import HttpResponseRedirect
from django.shortcuts import render , render_to_response
from django.core.context_processors import csrf

from django.template import RequestContext
from portalapp.models import *
from clubsapp.models import *
import requests
import json
import datetime, dateutil.parser
from django import template

register = template.Library()

def activityphoto(act_id):

    act = Activity.objects.filter(id = act_id)
    act_photo = ActivityPhotoRelationship.objects.filter(activity = act)
    phot = Photos.objects.filter(activityphotorelationship=act_photo)
    if phot is []:
        return
    if phot is None:
        return
    try:
        return phot[0].photograph.url
    except:
        return
register.filter('activityphoto',activityphoto)