csv_filepathname="Company Details for batch 2016-2017 (1).csv"

#Student_portal-company_table.csv
django_project_home = "C:\stupo\VNITClubs\studentportal"

import sys,os

sys.path.append(django_project_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'studentportal.settings'
print "bfr import models"
from clubsapp.models import Personinformation, ContactDetails, Photos, Post, ClubMember, Club, Event, Activity
from datetime import datetime
import pandas as pd




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

            club.save()



