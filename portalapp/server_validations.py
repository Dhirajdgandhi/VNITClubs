from .models import *
import re
#from SIP.models import ErrorContent
from datetime import datetime 
from datetime import *
from models import *
from django.core import serializers
from django.core.mail import send_mail

def isvalid_fname(fname):
	ck_fname = r"^[A-Za-z]{2,20}$" 
	if not fname:
		err_msg="First name not present "
	elif not re.match(ck_fname, fname):
		err_msg="First name not valid "
		err=2
	else:
		err_msg=""
	return err_msg

def isvalid_lname(lname):
	ck_lname = r"^[A-Za-z]{2,20}$" 
	if not lname:
		err_msg="Last name not present "
	elif not re.match(ck_lname, lname):
		err_msg="Last name not valid "
		err=2
	else:
		err_msg=""
	return err_msg

def isvalid_email(email):
	ck_email = r"^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$" 
	if not email:
		err_msg="Email not present "
	elif not re.match(ck_email, email):
		err_msg="Email name not valid "
		err=2
	else:
		err_msg=""
	return err_msg

def isvalid_phone(mob1,mob2):
	ck_mob= r"^[0-9]{10,10}$"
	err_msg=""
        print "mob2 "+mob2
	if not mob1:
		err_msg="first mobile number not present "
	elif not re.match(ck_mob,mob1):
		err_msg="first mobile number not valid "
	if mob2!="" and (not re.match(ck_mob,mob2)):
		err_msg=err_msg+"second mobile number not valid "
	return err_msg

def isvalid_clgid(clg_id):
	ck_clgid= r"^[0-9]{5}$" 
	err_msg=""
	if not clg_id:
		err_msg="College id not present "
	elif not re.match(ck_clgid, clg_id):
		err_msg="College id not valid "
		err=2
	else:
		err_msg=""
	return err_msg

def isvalid_rollno(roll_no):
	ck_rn1= r"^[B][T][0-9]{2}[A-Z]{3}[0-9]{3}$"
	ck_rn2= r"^[b][t][0-9]{2}[a-z]{3}[0-9]{3}$"
	err_msg=""
	if not roll_no:
		err_msg="Roll number not present "
	elif not re.match(ck_rn1, roll_no) and not re.match(ck_rn2, roll_no):
		err_msg="Roll number not valid "
		err=2
	else:
		err_msg=""
	return err_msg

def isvalid_dept(dept):
	if dept=="default":
		err_msg="Select a department"
	else:
		err_msg=""
	return err_msg

def isvalid_password_match(password1,password2):
	if len(password1) < 8:
 		err_msg="Length of password should atleast be 8 "
	elif password1 != password2:
		err_msg="passwords don't match "
	else:
		err_msg=""
	return err_msg

def isvalid_password(password):
	err_msg=""
	if password== "":
		err_msg="Please enter your password"
	elif len(password) < 8:
 		err_msg="Length of password should atleast be 8 "
	return err_msg


def isvalid_registraion(first_name,last_name,email,mob1,mob2,clg_id,dept,roll_no,password1,password2):
	err_msg=[isvalid_fname(first_name),isvalid_lname(last_name),isvalid_email(email),isvalid_phone(mob1,mob2),isvalid_clgid(clg_id),isvalid_rollno(roll_no),isvalid_dept(dept),isvalid_password_match(password1,password2)]
	return err_msg

def isvalid_companyid(company_id,new_company):
    err_msg=""
    if company_id=="":
        err_msg="Select a company or enter other company"
    elif (company_id=="other") and (new_company==""):
        err_msg="enter the other company name"
    print "oh"
    return err_msg
 
def isvalid_type(worktype):
	err_msg=""
	if worktype==-1:
		err_msg="Select a type"
	return err_msg


def isvalid_experience(company_id,new_company,worktype,package,rounds,cgpa,clg_id,dept_id):
	err_msg=isvalid_companyid(company_id,new_company)+isvalid_type(worktype)+isvalid_rounds(rounds)+isvalid_cgpa(cgpa)+isvalid_clgid(clg_id)+isvalid_dept(dept_id)
	return err_msg


def isvalid_login(clg_id,password):
	err_msg=[isvalid_clgid(clg_id),isvalid_password(password)]
	return err_msg


def isvalid_forgotpass(email,clg_id):
	err_msg=[isvalid_email(email),isvalid_clgid(clg_id)]
	return err_msg


def isvalid_dropdown(feild):
	err_msg=""
	if feild=="":
		err_msg="This feild cannot be empty."
	return err_msg

def isvalid_profile(profile):
    err_msg=""
    if profile=="not_selected":
        err_msg="Profile cannot be empty"
    return err_msg
 
def isvalid_package(package):
	ck_pckg= r"[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?" 
	err_msg=""
	print package
	package=str(package)
	if not re.match(ck_pckg, package):
		err_msg="Package amount not valid.Should be only numbers."
	print "her"
	return err_msg
	

def isvalid_cgpa(cgpa):   
    ck_cgpa= r"[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?" 
    print cgpa
    err_msg=""
    if not re.match(ck_cgpa, str(cgpa)):
		err_msg="CGPA  not valid.Should be only numbers."
    elif (int(float(cgpa))<0 or int(float(cgpa))>10):
		err_msg="Cgpa entered should be in range 0-10"
    print "here"
    return err_msg

def isvalid_rounds(rounds): 
	err_msg=""
	if rounds==0:
		err_msg="Choose number of rounds"
	return err_msg 

def isvalid_time(time):
	ck_time= r"^[0-9]{0,}$" 
	err_msg=0
	if not re.match(ck_time, str(time)):
		err_msg=1
	return err_msg


def isvalid_contribution(profile,company_id,new_company,package,cgpa,rounds,time_list):
     print "package ",package
     print "cgpa ",cgpa
     err_msg=[isvalid_companyid(company_id,new_company),isvalid_package(package),isvalid_cgpa(cgpa),isvalid_rounds(rounds)]
     if rounds!="": #For each round check details     
         for i in range(0,rounds-1):
             if isvalid_time(time_list[i]):
                 err_msg.append("Time of round "+str(i+1)+" not valid.Should only be numbers.")
     msg=[]
     for i in err_msg:
         if i!="":
             msg.append(i)
     return msg

def isvalid_oldpassword(oldpassword):
    err_msg=""
    if oldpassword== "":
		err_msg="Please enter your password"
    elif len(oldpassword) < 8:
 		err_msg="Length of old password should atleast be 8 "
    return err_msg

def isvalid_editprofile(fname,lname,tel1,tel2,oldpassword,pass1,pass2):
     err_msg=[isvalid_fname(fname),isvalid_lname(lname),isvalid_phone(tel1,tel2)]
     if len(oldpassword)>0:
         err_msg.append(isvalid_oldpassword(oldpassword))
     if len(pass1)>0:
         err_msg.append(isvalid_password_match(pass1,pass2))
     
     msg=[]
     for i in err_msg:
         if i!="":
             msg.append(i)
     return msg
