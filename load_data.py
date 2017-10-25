csv_filepathname="LoadCSVs\Club.csv"

#Student_portal-company_table.csv
django_project_home = "C:\stupo\VNITClubs\studentportal"

import sys,os

sys.path.append(django_project_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'studentportal.settings'
print "bfr import models"
from clubsapp.models import ContactDetails, Photos, Post, ClubMember, Club, Event, Activity
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
        club.president = row[6]
        club.clubType = row[7]
        club.facultyInCharge1 = row[8]
        club.facultyInCharge2 = row[9]
        club.contact = row[10]

        club.save()



