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
            contact = ContactDetails()
            contact.id = row[0]
            contact.email = row[1]
            contact.website = row[2]
            contact.telephone1 = row[3]
            contact.telephone2 = row[4]
            contact.save()
        '''



