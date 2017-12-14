'''
Loads all the gallery images from the folder
to the database by making sure of all the relationships
'''

django_project_home = "C:\stupo\VNITClubs\studentportal"

import sys,os
import random, string

sys.path.append(django_project_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'studentportal.settings'
print "bfr import models"
from clubsapp.models import *
print "aftr"
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

#for generate random string
def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

club = Club.objects.get(pk=12)
#location = 'images/12/' #before running the file uncomment the location
#os.chdir(location)
#os.getcwd()
for file in os.listdir(location):

    gall_img =  Photos()

    #spliting the extension of thr file
    extension = os.path.splitext(file)[1]
    #assign the name to file
    imgname = 'gallery_' + randomword(6) + str(extension)
    print file
    path = location + file
    #open the file
    handle = open(path, 'rb')
    #change to main directory
    #os.chdir('C:\stupo\VNITClubs')
    #saving the image
    gall_img.photograph.save(imgname, File(handle) )
    print "Saved"
    gall_img.details = 'gallery image for a club ' + str(club.id)
    print gall_img.details
    gall_img.save()

    club_photo = ClubPhotoRelationship()
    club_photo.photo = gall_img
    club_photo.club = club
    print club_photo
    club_photo.save()
    print "Done" + imgname
print"Complete Club"


