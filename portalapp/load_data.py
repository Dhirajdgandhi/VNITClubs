
csv_filepathname="Company Details for batch 2016-2017 (1).csv"
#CSE_Personal_data_testing.csv
#Student_portal-company_table.csv
django_project_home = "/home/portal/studentportal/studentportal/"

import sys,os

sys.path.append(django_project_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'studentportal.settings'
print "bfr import models"
from portalapp.models import Personinformation,Roles,ForLogin,company_table
from datetime import datetime
import pandas as pd




print "aftr" 
import csv
dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')

#r=Roles.objects.filter(short_name="Student").first()
for row in dataReader:
    if row[0] == 'id': # Ignore the header row, import everything 
        print 'Ignored the header'    
    else :
	'''	p=Personinformation()
		p.roleid=r
		p.email=row[2]
		p.firstname=row[3]
		p.lastname=row[4]
		p.telephone1=row[7]
		p.clg_id=row[5]
		p.deptid=1
		p.roll_no=row[6]
		#p.createdondate=
		p.save()

		l=ForLogin()
		l.clg_id=p
		l.password=id_generator()
		l.save()
	'''
	'''
	print row[1]
	c = company_table.objects.filter(company_name=row[1]).get()
	print c.company_name,row[1]
	#print datetime.strptime(row[10],'%d-%b-%Y')
	#print pd.to_datetime(row[10]).apply(lambda x: dt.datetime.strftime(x,'%m/%d/%y'))
	#print row[9]
	c.recentdate = row[10]
	c.save()
	'''
	c = company_table()
	# c.ID = row[0]
	c.company_name = row[1]
	print(c.company_name)
	c.short_name = row[2]
	c.long_name = row[3]
	c.display_name = row[4]
	
	c.intern_exp_count = int(row[5])
	c.job_exp_count = int(row[6])
	c.company_intern_valid = int(row[7])
	c.company_job_valid = int(row[8])
	c.startdate = row[9]
	#c.recentdate = row[10]
	c.valid = int(row[11])
	c.save()
	
		

	
	'''
        r = Profile_type()
        r.ID= row[0]
        r.display_name = row[1]
        r.description = row[2]

        r.save()
   '''     
