from django import template
from portalapp.models import *
from django.contrib.auth.hashers import *
import json

register = template.Library()

def key(obj, key_name):
    print key_name
    return getattr(obj,key_name)
    
key = register.filter('key', key)

def deptname(number):
    print number
    return Department.objects.filter(id=number).first().short_name
    
key = register.filter('deptname', deptname)

def urlencrypt(s):
    return base64.urlsafe_b64encode(s)
    
key = register.filter('urlencrypt', urlencrypt)

def round_details(obj, number):
    print 'number',number
    num = obj.num_of_rounds
    list=[]


    # p = (n for n in dir(obj) if n.endswith("_text"))

    if num >=1:
        dict1 = {'time': obj.round1_text.time, 'difficulty': obj.round1_text.difficulty.id, 'round_type': obj.round1_text.round_type.id,'description': obj.round1_text.description}
        list.append(dict1)
    if num >=2:
        dict2 = {'time': obj.round2_text.time, 'difficulty': obj.round2_text.difficulty.id, 'round_type': obj.round2_text.round_type.id,'description': obj.round2_text.description}
        list.append(dict2)
    if num >=3:
        dict3 = {'time': obj.round3_text.time, 'difficulty': obj.round3_text.difficulty.id, 'round_type': obj.round3_text.round_type.id,'description': obj.round3_text.description}
        list.append(dict3)
    if num >=4:
        dict4 = {'time': obj.round4_text.time, 'difficulty': obj.round4_text.difficulty.id, 'round_type': obj.round4_text.round_type.id,'description': obj.round4_text.description}
        list.append(dict4)
    if num >=5:
        dict5 = {'time': obj.round5_text.time, 'difficulty': obj.round5_text.difficulty.id, 'round_type': obj.round5_text.round_type.id,'description': obj.round5_text.description}
        list.append(dict5)
    if num >=6:
        dict6 = {'time': obj.round6_text.time, 'difficulty': obj.round6_text.difficulty.id, 'round_type': obj.round6_text.round_type.id,'description': obj.round6_text.description}
        list.append(dict6)


    # for round in obj.num_of_rounds:
    print json.dumps(str(list))
    return json.dumps(list)
    # return dict

    # return [{'time':40,'description':60}]

key = register.filter('round_details', round_details)
