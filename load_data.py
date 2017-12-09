csv_filepathname="LoadCSVs\Club.csv"
#csv_filepathname="LoadCSVs\ContactDetails.csv"
django_project_home = "C:\stupo\VNITClubs\studentportal"

import sys,os

sys.path.append(django_project_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'studentportal.settings'
print "bfr import models"
from clubsapp.models import *
from datetime import datetime


print "aftr"
import csv
dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')

#iterate over each row
for row in dataReader:
    if row[0] == 'id':  # Ignore the header row, import everything
        print 'Ignored the header'
    else:

        club = Club()
        club.id = row[0]
        club.shortName = row[1]
        club.longName = row[2]
        club.displayName = row[3]
        club.aboutUs = row[4]
        club.yearOfStart = row[5]
        personInfoObject = Personinformation.objects.get(clg_id=15616)
        print personInfoObject
        club.president = personInfoObject
        club.clubType = row[7]
        club.facultyInCharge1 = row[8]
        club.facultyInCharge2 = row[9]
        contact_detail = ContactDetails.objects.get(id=row[10])
        print contact_detail
        club.contact = contact_detail
        club.save()

        '''
        clubmember = ClubMember()
        clubmember.id = row[0]
        clubmember.basicDetails = row[1]
        memberPost = Post.object.get(id=row[2])
        print memberPost
        clubmember.post = memberPost
        clubmember.photograph = row[3]
        clubmember.dateOfJoin = row[4]
        clubmember.dateOfLeave = row[5]
        clubmember.save()
        

        contact = ContactDetails()
        contact.id = row[0]
        contact.email = row[1]
        contact.website = row[2]
        contact.telephone1 = row[3]
        contact.telephone2 = row[4]
        contact.save()

        post = Post()
        post.id = row[0]
        post.shortName = row[1]
        post.longName = row[2]
        post.displayName = row[3]
        post.save()

        photos = Photos()
        photos.id = row[0]
        photos.photographs = row[1]
        photos.details = row[2]
        photos.dateOfCapture = row[3]
        photos.save()

        event = Event()
        event.id = row[0]
        event.shortName = row[1]
        event.longName = row[2]
        event.displayName = row[3]
        event.place = row[4]
        event.time = row[5]
        event.date = row[6]
        event.save()

        activity = Activity()
        activity.id = row[0]
        activity.title = row[1]
        activity.description = row[2]
        activity.date = row[3]
        activity.save()

        cer = ClubEventRelationship()
        cer.id = row[0]
        cerclub = Club.object.get(id=row[1])
        print cerclub
        cer.club = cerclub
        cerevent = Event.object.get(id=row[2])
        print cerevent
        cer.event = cerevent
        cer.save()

        car = ClubActivityRelationship()
        car.id = row[0]
        carclub = Club.object.get(id=row[1])
        print carclub
        car.club = carclub
        caractivity = Activity.object.get(id=row[2])
        print caractivity
        car.activity = caractivity
        car.save()

        cpr = ClubPhotoRelationship()
        cpr.id = row[0]
        cprclub = Club.object.get(id=row[1])
        print cprclub
        cpr.club = cprclub
        cprphoto = Photos.object.get(id=row[2])
        print cprphoto
        cpr.photo = cprphoto
        cpr.save()

        epr = EventPhotoRelationship()
        epr.id = row[0]
        eprevent = Event.object.get(id=row[1])
        print eprevent
        epr.event = eprevent
        eprphoto = Photos.object.get(id=row[2])
        print eprphoto
        epr.photo = eprphoto
        epr.save()

        apr = ActivityPhotoRelationship()
        apr.id = row[0]
        apractivity = Activity.object.get(id=row[1])
        print apractivity
        apr.activity = apractivity
        aprphoto = Photos.object.get(id=row[2])
        print aprphoto
        apr.photo = aprphoto
        apr.save()
        '''











