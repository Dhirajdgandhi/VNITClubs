#from tnp.forms import RegistrationForm
from django.core.exceptions import ObjectDoesNotExist

from portalapp.models import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required
#from django.contrib.auth import login,logout 
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response,render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.contrib.auth.hashers import *
from django.contrib.auth.models import check_password
import server_validations
from django.core.mail import send_mail
from django.core import serializers
from django.template import loader # Sending html page as email
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.core.serializers.json import DjangoJSONEncoder
import json
import datetime

FROM_EMAIL = 'studentportal.vnit@gmail.com'

# HTTP Error 404
def page_not_found(request):
	response = render_to_response('404.html', context_instance=RequestContext(request) )
  	response.status_code = 404
   	return response

# HTTP Error 500
def server_error(request):
	response = render_to_response('500.html',context_instance=RequestContext(request))
   	response.status_code = 500
   	return response


s="1"
s1=base64.urlsafe_b64encode(s)
print s,s1
s2=base64.urlsafe_b64decode(s1)
print s2

@csrf_protect
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def aboutus(request):
    args = {'page_name':"About us"}
    args.update(csrf(request))
    args.update(headerdb(request))

    return render_to_response('aboutus.html',args)


@csrf_protect
def register(request):
	if request.method == 'POST':
          roleid=Roles.objects.filter(long_name="Student").first() #bydefault student
          email = request.POST.get('email','')
          first_name = request.POST.get('fname','')
          last_name = request.POST.get('lname','')
          mob1= request.POST.get('telephone1','')
          mob2= request.POST.get('telephone2','')
          clg_id=request.POST.get('clg_id' ,'')
          dept=int(request.POST.get('dept',''))
          print dept
          roll_no = request.POST.get('roll_no','')
          password1 = request.POST.get('password1','')
          password2 = request.POST.get('password2','')
          #Currently storing password with encryption :
          x=make_password( password1 )
          #Server side validations - for fields as well checking if user already exists
          err_msg=[]
          if clg_id!="":
              user=ForLogin.objects.filter(clg_id=clg_id).first()
          else:
              user=None

          if user is not None:
              print user
              print "User already registered"
              #return HttpResponseRedirect('/success/')
              err_msg=["user with this college id already exists"]

          err_msg=(err_msg)+server_validations.isvalid_registraion(first_name,last_name,email,mob1,mob2,clg_id,dept,roll_no,password1,password2)

          interface_obj = Personinformation(roleid=roleid,clg_id=clg_id,deptid=dept,roll_no=roll_no,email=email,firstname=first_name,lastname=last_name,telephone1=mob1,telephone2=mob2,is_active=1,createdondate=datetime.datetime.now())
          open_modal1=2 #Default value- nothing opens
          flag=0
          for i in err_msg:
        		if i!="":
        			flag=1

          if flag: #if any error
              open_modal1=1 #Register modal
              password1=""
              password2=""
              print "asdf"
              print open_modal1

              args={'open_modal1':open_modal1,'err_msg':err_msg,'register_fname':first_name,'lname':last_name,'email':email,'mob1':mob1,'mob2':mob2,'register_clg_id':clg_id,'dept':dept,'roll_no':roll_no,'password1':password1,'password2':password2}
              args.update(headerdb(request))
              print "111111111111"
              return render(request,'homepage.html',args)

          #Else save person if no error
          interface_obj.save()

          print Personinformation.objects.all()
          print interface_obj.clg_id

          #If its a foreign key we need to save in it an instance i.e an object --> it properly extracts the primary key from it.
          interface_obj = ForLogin(clg_id=interface_obj,password=x)
          interface_obj.save()

          user=ForLogin.objects.filter(clg_id=clg_id)
          print user

          return HttpResponseRedirect('/home/?register_success='+str(1))

	else:
	     fname=""
    	     open_modal1=1 #Login modal
	     args={'fname':fname,'open_modal1':open_modal1}
	     args.update(headerdb(request))
             args.update({'fname':"",'lname':"",'email':"",'mob1':"",'mob2':"",'clg_id':"",'dept':"",'roll_no':"",'password1':"",'password2':""})

	     return render(request,'homepage.html',args)




@csrf_protect
def success(request):
        args = {}
        args.update(csrf(request))
        return render_to_response(
        'success.html',args
        )


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def login(request):
	if request.method == 'POST':
         clg_id=request.POST.get('usrname' ,'')
         password = request.POST.get('psw','')
	 err_msg=server_validations.isvalid_login(clg_id,password)
	 print err_msg
	 flag=0
         for i in err_msg:
        		if i!="":
        			flag=1

	 if flag==0:
		 user = ForLogin.objects.filter(clg_id=clg_id).first()

		 if user is not None:
			 #Currently checking encrypted password : check_password(password,user.password) #password==user.password
			 if (check_password(password,user.password)):
				 request.session['clg_id']=clg_id #Creating a session
		                 loginas = user.clg_id.roleid.long_name
				 print loginas
				 request.session['loginas'] = loginas #Session for the logged in user role
				 return HttpResponseRedirect('/home/')
			 else:
				 fname=""
		     	 	 err_msg=["Wrong password"]
		     		 open_modal1=4 #Login modal
		     		 args={'fname':fname,'open_modal1':open_modal1,'err_msg_log':err_msg,'clg_id':clg_id}
		     		 args.update(headerdb(request))
		                 return render(request,'homepage.html',args)
		 else:
		     fname=""
		     print "uivp"
		     err_msg=["User with this username does not exist"]
		     open_modal1=4 #Login modal
		     args={'fname':fname,'open_modal1':open_modal1,'err_msg_log':err_msg,'clg_id':clg_id}
		     args.update(headerdb(request))
		     return render(request,'homepage.html',args)
	 else:
	     fname=""
	     print "frontend error"
	     open_modal1=4 #Login modal
	     args={'fname':fname,'open_modal1':open_modal1,'err_msg_log':err_msg,'clg_id':clg_id}
	     args.update(headerdb(request))
	     return render(request,'homepage.html',args)


        else:
	     fname=""
	     open_modal1=4 #Login modal
	     args={'fname':fname,'open_modal1':open_modal1}
	     args.update(headerdb(request))
	     return render(request,'homepage.html',args)



@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def logout(request):
    try:
        del request.session['clg_id']
        del request.session['loginas']
	logout(request)
    except KeyError:
        pass
    return HttpResponseRedirect('/home/')

'''  new forgot password Atharva '''
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def resetpass(request, fkey):
   if request.method == 'POST':
       # clg_id = base64.urlsafe_b64decode(clg_id.encode("ascii"))
       # print
       # clg_id
       pass1 = request.POST.get('pass1', '')
       pass2 = request.POST.get('pass2', '')
       if len(pass1) >= 8:
           if pass1 == pass2:
               # obj1 = Personinformation.objects.filter(clg_id=clg_id).first()
               try:
                   fpk_obj = ForgotPassKeys.objects.get(key=fkey, is_valid=True)
                   obj1 = fpk_obj.user
                   obj = ForLogin.objects.filter(clg_id=obj1).first()
                   obj.password = make_password(pass1)
                   fpk_obj.is_valid = False
                   fpk_obj.save()
                   # print
                   # obj.password
                   obj.save()
                   return HttpResponseRedirect('/home/')
               except ForgotPassKeys.DoesNotExist:
                   pass
                   '''err_msg = "Link is either expired or invalid"
                   args = {'err_msg': err_msg}
                   args.update(headerdb(request))
                   args.update(csrf(request))
                   return render_to_response('resetpass.html', args)'''
           else:
               err_msg = "passwords dont match"
               args = {'err_msg': err_msg}
               args.update(headerdb(request))
               args.update(csrf(request))
               return render_to_response('resetpass.html', args)
       else:
           err_msg = "minimum 8 characters required"
           args = {'err_msg': err_msg}
           args.update(headerdb(request))
           args.update(csrf(request))
           args.update({'page_name':'Reset Password'})
           return render_to_response('resetpass.html', args)

   # else : return HttpResponseRedirect('/forgetpass/%d' clg_id)
   try:
       fpk_obj = ForgotPassKeys.objects.get(key=fkey, is_valid=True)
       args = {}
       args.update(headerdb(request))
       args.update(csrf(request))
       args.update({'page_name':'Reset Password'})
       return render_to_response('resetpass.html', args)
   except ForgotPassKeys.DoesNotExist:
       fname = ""
       err_msg = ["Invalid or Expired link"]
       open_modal1 = 5
       args = {'fname': fname, 'open_modal1': open_modal1, 'err_msg_fp': err_msg,}
       args.update(headerdb(request))
       return render(request, 'homepage.html', args)


'''
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def resetpass(request,clg_id):
    if request.method == 'POST':
           clg_id = base64.urlsafe_b64decode(clg_id.encode("ascii"))
           print clg_id
           pass1 = request.POST.get('pass1','')
           pass2 = request.POST.get('pass2','')
           if len(pass1) >= 8:
			 if pass1==pass2 :
		          obj1 = Personinformation.objects.filter(clg_id=clg_id).first()
		          obj=ForLogin.objects.filter(clg_id=obj1).first()
		          
		          obj.password=make_password(pass1)  
		          print obj.password
		          obj.save()
            
                    
		          return HttpResponseRedirect('/home/')
			 else:
			  err_msg="passwords dont match"
			  args = {'err_msg':err_msg}
    			  args.update(headerdb(request))
    			  args.update(csrf(request))    
    			  return render_to_response('resetpass.html',args)
           else:
    		  err_msg="minimum 8 characters required"
		  args = {'err_msg':err_msg}
    		  args.update(headerdb(request))
    		  args.update(csrf(request))    
    		  return render_to_response('resetpass.html',args)
		  
		
          
   #else :- return HttpResponseRedirect('/forgetpass/%d' clg_id)
   
    args = {}
    args.update(headerdb(request))
    args.update(csrf(request))    
    return render_to_response('resetpass.html',args)
'''

'''  new forgot password Atharva '''
def forgotpass(request):
   if request.method == "POST":
       clg_id = request.POST.get('clg_id')
       email = request.POST.get('email')
       err_msg = server_validations.isvalid_forgotpass(email, clg_id)
       print err_msg
       flag = 0
       for i in err_msg:
           if i != "":
               flag = 1
               # fname = ""

       if flag == 0:
           if Personinformation.objects.filter(clg_id=clg_id).first() is not None:
               if Personinformation.objects.filter(clg_id=clg_id, email=email).first() is not None:
                   # link = request.META['HTTP_HOST']+"/resetpass/%s" %clg_id
                   # email_msg="Click on the following link to reset your password:
                   # \n"+request.META['HTTP_HOST']+"/resetpass/%s" % base64.urlsafe_b64encode(clg_id)
                   # emailobj = Personinformation.objects.filter(clg_id=clg_id).first()
                   # New Forgot Password Implementation by Atharva
                   person_obj = Personinformation.objects.get(clg_id=clg_id)
                   email = person_obj.email
                   try:
                       fpk_obj = ForgotPassKeys.objects.get(user=person_obj, is_valid=True)
                       uid = fpk_obj.key
                   except ForgotPassKeys.DoesNotExist:
                       uid = get_random_string(length=10)
                       forgotpasskey_obj = ForgotPassKeys()
                       forgotpasskey_obj.user = person_obj
                       forgotpasskey_obj.key = uid
                       forgotpasskey_obj.save()

                   # person_obj=Personinformation.objects.filter(clg_id=clg_id).first()
                   # link = request.META['HTTP_HOST']+"/resetpass/%s" % base64.urlsafe_b64encode(clg_id)
                   link = request.META['HTTP_HOST'] + "/resetpass/" + uid
                   email_msg = loader.render_to_string('password_reset_email.html',
                                                       {'name': person_obj.firstname, 'link': link})
                   # password_reset_email.html
                   send_mail('student portal password reset', "This is it", FROM_EMAIL,
                             [email], html_message=email_msg)
                   return HttpResponseRedirect('/home/?forgotpass_emailsent='+str(1))
               else:
                   fname = ""
                   err_msg = ["Wrong combination of email and clgid"]
                   open_modal1 = 5
                   args = {'fname': fname, 'open_modal1': open_modal1, 'err_msg_fp': err_msg, 'clg_id': clg_id}
                   args.update(headerdb(request))
                   return render(request, 'homepage.html', args)
           else:
               fname = ""
               err_msg = ["User not registered"]
               open_modal1 = 5
               args = {'fname': fname, 'open_modal1': open_modal1, 'err_msg_fp': err_msg, 'clg_id': clg_id}
               args.update(headerdb(request))
               return render(request, 'homepage.html', args)
       else:
           fname = ""
           err_msg = "Something went wrong"
           # print "frontend error"
           open_modal1 = 5  # forgot pass modal
           args = {'fname': fname, 'open_modal1': open_modal1, 'err_msg_fp': err_msg, 'clg_id': clg_id}
           args.update(headerdb(request))
           return render(request, 'homepage.html', args)

   fname = ""
   # print "frontend error"
   open_modal1 = 5  # forgot pass modal
   args = {'fname': fname, 'open_modal1': open_modal1}
   args.update(headerdb(request))
   return render(request, 'homepage.html', args)



''' 
def forgotpass(request):
    if request.method == "POST":
        clg_id = request.POST.get('clg_id') 
        email = request.POST.get('email')
	err_msg=server_validations.isvalid_forgotpass(email,clg_id)
	print err_msg
	flag=0
        for i in err_msg:
        		if i!="":
        			flag=1

	fname=""
	if flag==0:
		if Personinformation.objects.filter(clg_id=clg_id).first() is not None:
		    if Personinformation.objects.filter(clg_id=clg_id,email=email).first() is not None:    
		        #link = request.META['HTTP_HOST']+"/resetpass/%s" %clg_id
			#email_msg="Click on the following link to reset your password: \n"+request.META['HTTP_HOST']+"/resetpass/%s" % base64.urlsafe_b64encode(clg_id)
		        emailobj = Personinformation.objects.filter(clg_id=clg_id).first()
		        email = emailobj.email
			person_obj=Personinformation.objects.filter(clg_id=clg_id).first()
			link=request.META['HTTP_HOST']+"/resetpass/%s" % base64.urlsafe_b64encode(clg_id)
			email_msg = loader.render_to_string('password_reset_email.html',{'name':person_obj.firstname,'link':link }) #password_reset_email.html
		        send_mail('student portal password reset',"This is it", FROM_EMAIL, [email],html_message=email_msg)

		        
		        return HttpResponseRedirect('/home/?forgotpass_emailsent='+str(1))
		    else:
			fname=""
		        err_msg=["Wrong combination of email and clgid"]
		        open_modal1=5
		     	args={'fname':fname,'open_modal1':open_modal1,'err_msg_fp':err_msg,'clg_id':clg_id}
		     	args.update(headerdb(request))
		     	return render(request,'homepage.html',args)
		else:
		    fname=""
		    err_msg=["User not registered"]
		    open_modal1=5
	     	    args={'fname':fname,'open_modal1':open_modal1,'err_msg_fp':err_msg,'clg_id':clg_id}
	     	    args.update(headerdb(request))
	     	    return render(request,'homepage.html',args)
	else:
	    fname=""
	    print "frontend error"
	    open_modal1=5 #forgot pass modal
	    args={'fname':fname,'open_modal1':open_modal1,'err_msg_fp':err_msg,'clg_id':clg_id}
	    args.update(headerdb(request))
	    return render(request,'homepage.html',args)
    else:	
	fname=""
	print "frontend error"
	open_modal1=5 #forgot pass modal
	args={'fname':fname,'open_modal1':open_modal1}
	args.update(headerdb(request))
	return render(request,'homepage.html',args)
'''


def headerdb(request):
    if 'clg_id' in request.session:
        clg_id=request.session['clg_id']
        fname=Personinformation.objects.filter(clg_id=clg_id).first().firstname
        loginas = request.session['loginas']
        cannot_contribute = 0
        forgotpass_emailsent =0
        contribute_success = request.GET.get('contribute_success')
	experience_saved = request.GET.get('experience_saved')
        register_success = 0
    else:
        fname=""
        clg_id=""
        loginas=""
        cannot_contribute=request.GET.get('cannot_contribute')
        forgotpass_emailsent=request.GET.get('forgotpass_emailsent','0')
        register_success = request.GET.get('register_success')
	experience_saved=0
        contribute_success = 0
    #Getting the top 8 departmetn objects only as they are the distinct department
    dept_list=Department.objects.all().order_by('id')[:8]

    intern_company_list=company_table.objects.filter(company_intern_valid=1,valid=1)
    job_company_list=company_table.objects.filter(company_job_valid=1,valid=1)
    #print dept_list
      # List of experiences '''
    exp_intern_list=experience_internship.objects.filter(valid=1).order_by('-timestamp') # The '-' sign is for descending ordering.
    exp_job_list =experience_placement.objects.filter(valid=1).order_by('-timestamp')

    print exp_job_list
    ''' Pagination '''
    '''paginator = Paginator(exp_intern_list,4) #Show 1 experience per page
    
    page = request.GET.get('page')
    try:
        exp_intern_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        exp_intern_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        exp_intern_list = paginator.page(paginator.num_pages)'''
    ''' End of pagination '''

    context_ins={'loginas':loginas,'header_dept_list':dept_list,'dept_list':dept_list,
                  'header_intern_company_list':intern_company_list,
		 'header_job_company_list':job_company_list,
		 'exp_intern_list':exp_intern_list,
		 'exp_job_list':exp_job_list,'experience_saved':experience_saved, 'fname':fname,'clg_id':clg_id,'register_success':register_success,'cannot_contribute':cannot_contribute,'forgotpass_emailsent':forgotpass_emailsent,'contribute_success':contribute_success }

    return context_ins

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def add_program(request):
    program_name = request.POST.get('program_name','');
    degree_level = request.POST.get('degree_level','');
    clgid = request.session['clg_id']

    deptid = Personinformation.objects.get(clg_id=clgid).deptid
    deptobj = Department.objects.get(id=deptid)

    newdeptobj = Department(short_name=deptobj.short_name,long_name=deptobj.short_name,display_name=deptobj.display_name,program=program_name,degree_level=degree_level)
    newdeptobj.save()

    return HttpResponseRedirect('/home/')


def homepage(request):
    if request.method == "POST":
        #print request.session['fname']
        print "was successfully Logged out"
        return logout(request)

    context_ins={'open_modal1':3}
    context_ins.update(headerdb(request))

    if context_ins['loginas'] == "HOD":
        ''' to display the programs of the HOD '''
        clg_id = request.session['clg_id']
        deptid = Personinformation.objects.get(clg_id=clg_id).deptid
        short_name = Department.objects.get(id=deptid).short_name
        deptobj = Department.objects.filter(short_name=short_name)

        context_ins['deptobj'] = deptobj

    context_ins['page_name']="homepage"
    args = {}
    args.update(csrf(request))
    return render_to_response(
    'homepage.html',context_ins,context_instance=RequestContext(request)
    )


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def company_placements(request,comp_id=0):
        comp_id=int(comp_id)
        #The compid is the Company id you are referencing to.
        comp_obj=company_table.objects.filter(id=comp_id,valid=1).first()

        jobs_cdr=Company_Department_Relation.objects.filter(company_id=comp_id,job_valid=1)
        jobs_exp=[]
        for i in jobs_cdr:
            jobs_exp=jobs_exp+list(experience_placement.objects.filter(cdr_id=i.id,valid=1))
        jobs_exp=sorted(jobs_exp, key=lambda x: x.timestamp, reverse=True)

        page_name = comp_obj.display_name + " | Placements"
        args = {'page_name':page_name,'jobs':jobs_exp,'comp_obj':comp_obj}

        args.update(headerdb(request))
        args.update(csrf(request))
        return render_to_response(
        'company_placement.html',args)


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def company_internships(request,comp_id=0):
        comp_id=int(comp_id)
        comp_obj=company_table.objects.filter(id=comp_id,valid=1).first()
        print comp_obj.company_name
        interns_cdr=Company_Department_Relation.objects.filter(company_id=comp_id,intern_valid=1)
        interns_exp=[]
        for i in interns_cdr:
            interns_exp=interns_exp+list(experience_internship.objects.filter(cdr_id=i.id,valid=1))
        interns_exp=sorted(interns_exp, key=lambda x: x.timestamp, reverse=True)

        page_name = comp_obj.display_name + " | Internships"
        args = {'page_name':page_name,'interns':interns_exp,'comp_obj':comp_obj}
        args.update(headerdb(request))
        args.update(csrf(request))
        return render_to_response(
        'company_internships.html',args)


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def fill_experience(request):
  if request.method=="POST":
    	edit_expid = request.GET.get('edit_exp')
        type = request.GET.get('type')
        if request.POST.get('submit'):
            print "submit"
        if request.POST.get('save'):
            print "save"
        worktype = int(request.POST.get('type')) # 0-intern , 1-job
        profile = Profile_type.objects.filter(id=request.POST.get('profile')).first()
        criteria = request.POST.get('criteria','Not mentioned')
        company_id = request.POST.get('company')
        new_company = request.POST.get('new_company')
        where = int(request.POST.get('On-Off campus'))
        clg_id = request.session['clg_id']
        package = request.POST.get('package')
        cgpa = request.POST.get('cgpa')
        selected = request.POST.get('selected')

        if package == "":
            package = 0
        elif package.isdigit():
            package = float(package)*float(request.POST.get('amount'))

        if cgpa == "" :
            cgpa = 0
        elif cgpa.isdigit():
            cgpa = float(cgpa)

        rounds = request.POST.get('rounds')
        session=request.POST.get('session') #2016-17

        #server
        time_list=[]
        if rounds!=0:
            for i in range(0,int(rounds)-1):
                time_list.append(request.POST.get('round'+str(i+1)+'time'))
        print time_list

        err_msg=server_validations.isvalid_contribution(profile,company_id,new_company,package,cgpa,int(rounds),time_list)
        print err_msg

        if len(err_msg)!=0:
            comp_list = company_table.objects.only("company_name","id")

            difficulty_obj = Difficulty_type.objects.all()
            round_type = InterviewRound_type.objects.all()
            profile_type = Profile_type.objects.all()

            Context = {'profile_type':profile_type,'difficulty_obj':difficulty_obj,'round_type':round_type,'page_name':"Write your experience",'comp_list':comp_list}
            Context.update(headerdb(request))

            edit_exp = experience_internship.objects.filter(id=edit_expid).first()
            if edit_exp:
                Context.update({'edit_exp':edit_exp})
            else:
            	 edit_exp = experience_placement.objects.filter(id=edit_expid).first()
            	 if edit_exp:
                	Context.update({'edit_exp':edit_exp})
            Context.update(csrf(request))

            Context.update({'err_msg':err_msg})
            return render_to_response(
        'experienceform.html',Context,context_instance=RequestContext(request)
        )

        deptid = Personinformation.objects.get(clg_id=clg_id).deptid
        deptobj = Department.objects.get(id=deptid)


        cdr_obj=None
        if request.POST.get('submit'):
            # On submit - IF its a new company then add it to the list
            if new_company != "":
                #should send some notification to admin that new company is added and add its other details (with proper it is for intern or job)!!!!!!!!!!!!!!!!!
                interface_obj = company_table(company_name=new_company,intern_exp_count=0,job_exp_count=0,startdate = datetime.datetime.now(),valid=0)
                interface_obj.save()
                company_id = interface_obj.id #get the id of the newly created object

            company = company_table.objects.filter(id=company_id).first()
            ''' Do once exp is accepted
            if worktype==0:
                    company.company_intern_valid=1
            elif worktype==1:
                    company.company_job_valid=1

            company.save()
            '''
            cdr_obj=Company_Department_Relation.objects.filter(deptid=deptobj,company_id=company,session=session).first()
            print cdr_obj
            #Already existing company with the proper session and department
            if cdr_obj is not None:
                print cdr_obj
                ''' Do once exp is accepted
                if worktype==0:
                      cdr_obj.intern_valid=1
                elif worktype==1:
                        cdr_obj.job_valid=1

                cdr_obj.save()
                '''



        round1=round2=round3=round4=round5=round6=None
        rounds=int(rounds)
        if(rounds>=1):
            round_object =  InterviewRound_details(time=request.POST.get('round1time'),difficulty=Difficulty_type.objects.filter(id=request.POST.get('round1level')).first(),round_type=InterviewRound_type.objects.filter(id=request.POST.get('round1type')).first(),description=request.POST.get('round1'))
            round_object.save()
            round1=InterviewRound_details.objects.filter(id=round_object.id).first()

        if(rounds>=2):
           round_object =  InterviewRound_details(time=request.POST.get('round2time'),difficulty=Difficulty_type.objects.filter(id=request.POST.get('round2level')).first(),round_type=InterviewRound_type.objects.filter(id=request.POST.get('round2type')).first(),description=request.POST.get('round2'))
           round_object.save()
           round2=InterviewRound_details.objects.filter(id=round_object.id).first()

        if(rounds>=3):
           round_object =  InterviewRound_details(time=request.POST.get('round3time'),difficulty=Difficulty_type.objects.filter(id=request.POST.get('round3level')).first(),round_type=InterviewRound_type.objects.filter(id=request.POST.get('round3type')).first(),description=request.POST.get('round3'))
           round_object.save()
           round3=InterviewRound_details.objects.filter(id=round_object.id).first()

        if(rounds>=4):
           round_object =  InterviewRound_details(time=request.POST.get('round4time'),difficulty=Difficulty_type.objects.filter(id=request.POST.get('round4level')).first(),round_type=InterviewRound_type.objects.filter(id=request.POST.get('round4type')).first(),description=request.POST.get('round4'))
           round_object.save()
           round4=InterviewRound_details.objects.filter(id=round_object.id).first()

        if(rounds>=5):
           round_object =  InterviewRound_details(time=request.POST.get('round5time'),difficulty=Difficulty_type.objects.filter(id=request.POST.get('round5level')).first(),round_type=InterviewRound_type.objects.filter(id=request.POST.get('round5type')).first(),description=request.POST.get('round5'))
           round_object.save()
           round5=InterviewRound_details.objects.filter(id=round_object.id).first()

        if(rounds>=6):
          round_object =  InterviewRound_details(time=request.POST.get('round6time'),difficulty=Difficulty_type.objects.filter(id=request.POST.get('round6level')).first(),round_type=InterviewRound_type.objects.filter(id=request.POST.get('round6type')).first(),description=request.POST.get('round6'))
          round_object.save()
          round6=InterviewRound_details.objects.filter(id=round_object.id).first()


        if worktype==0:
            internship=1
            job=0
        else:
            job=1
            internship=0

        other_comments = request.POST.get('other_comments')
        fie = open("r.txt", "w")
        fie.write(str(other_comments))
        fie.close()
		#other_comments = request.POST['other_comments']


        #get user object:
        userobj = Personinformation.objects.filter(clg_id=clg_id).first()
        #acc to internship and job store it in tables

        #Intern experience
        if worktype==0:
            if edit_expid: #If person is submitting or editing an already added experience then just update detail
                interface_obj=experience_internship.objects.filter(id=edit_expid)
                interface_obj.update(selected=selected, onoffcampus=where, profile=profile,
                                                  criteria=criteria, package=package, cdr_id=cdr_obj, cgpa=cgpa,
                                                  userid=userobj, num_of_rounds=rounds, round1_text=round1,
                                                  round2_text=round2, round3_text=round3, round4_text=round4,
                                                  round5_text=round5, round6_text=round6, other_comments=other_comments, timestamp=datetime.datetime.now())
                interface_obj=interface_obj.first()
            else: #Else create a new object
                interface_obj = experience_internship(selected=selected,onoffcampus=where,profile=profile,criteria=criteria,package=package,cdr_id=cdr_obj,cgpa=cgpa,userid=userobj,num_of_rounds=rounds,round1_text=round1,round2_text=round2,round3_text=round3,round4_text=round4,round5_text=round5,round6_text=round6,other_comments=other_comments)
            interface_obj.save()

            if cdr_obj is not None  :
                print cdr_obj
                ''' Do once exp is accepted
                company.intern_exp_count += 1 #increment the count of experiences for that company object 
                company.save()
                '''
            if request.POST.get('submit'):
                if new_company != "" or (cdr_obj is None): # new_request for a company or a session
                    print "New"
                    requests_obj = Requests(session=session,intern_exp_id = interface_obj,company_id=company,status=0)
                    requests_obj.save()
                interface_obj.valid=0
                interface_obj.save()
            else:
                interface_obj.valid=3
                interface_obj.save()
        else: #Job experience
            if edit_expid:  # If person is submitting or editing an already added experience then just update detail
                interface_obj = experience_placement.objects.filter(id=edit_expid)
                interface_obj.update(selected=selected, onoffcampus=where, profile=profile,
                                     criteria=criteria, package=package, cdr_id=cdr_obj, cgpa=cgpa,
                                     userid=userobj, num_of_rounds=rounds, round1_text=round1,
                                     round2_text=round2, round3_text=round3, round4_text=round4,
                                     round5_text=round5, round6_text=round6, other_comments=other_comments, timestamp=datetime.datetime.now())
                interface_obj = interface_obj.first()
            else:  # Else create a new object
                interface_obj = experience_placement(selected=selected,onoffcampus=where,profile=profile,criteria=criteria,package=package,cdr_id=cdr_obj,cgpa=cgpa,userid=userobj,num_of_rounds=rounds,round1_text=round1,round2_text=round2,round3_text=round3,round4_text=round4,round5_text=round5,round6_text=round6,other_comments=other_comments)
            interface_obj.save()

            if cdr_obj is not None :
                print cdr_obj
                ''' Do once exp is accepted
                company.job_exp_count += 1 #increment the count of experiences for that company object 
                company.save()
                '''
            if request.POST.get('submit'):
                if new_company != "" or (cdr_obj is None): # new_requests
                    requests_obj = Requests(session=session,job_exp_id = interface_obj,company_id=company,status=0)
                    requests_obj.save()
                interface_obj.valid = 0
                interface_obj.save()
            else:
                interface_obj.valid = 3
                interface_obj.save()

        if request.POST.get('submit'):
            ''' Mail to user '''
            clg_id = userobj.clg_id
            email = userobj.email
            link=request.META['HTTP_HOST']+"/home"
            html_msg = loader.render_to_string('contribute_email.html',{'name':userobj.firstname,'link':link })
            send_mail('Response from Student Portal',"Hello", FROM_EMAIL, [email],html_message=html_msg)
            ''' Finish Mail to user '''

            return HttpResponseRedirect('/home/?contribute_success='+str(1))
        else:
            print "Cool"
            return HttpResponseRedirect('/home/?experience_saved=' + str(1))


  if 'clg_id' in request.session:
        comp_list = company_table.objects.filter(valid=1).only("company_name", "id").order_by("company_name")
        difficulty_obj = Difficulty_type.objects.all()
        round_type = InterviewRound_type.objects.all()
        profile_type = Profile_type.objects.all()

        Context = {'profile_type': profile_type, 'difficulty_obj': difficulty_obj, 'round_type': round_type,
                   'comp_list': comp_list}
        Context.update(headerdb(request))
        Context.update(csrf(request))


        ''' Check if already saved experience exists and if so, redirect to saved exp page. '''
        clg_id = request.session['clg_id']
        # get user object
        userobj = Personinformation.objects.filter(clg_id=clg_id).first()

        saved_intern_exp = experience_internship.objects.filter(userid=clg_id, valid=3)
        saved_job_exp = experience_placement.objects.filter(userid=clg_id, valid=3)
        #print saved_intern_exp,saved_job_exp

        Context.update({'saved_intern_exp': saved_intern_exp, 'saved_job_exp': saved_job_exp})

        new_exp = request.GET.get('new_exp')
        if new_exp:
            new_exp=int(new_exp)
        else:
            new_exp=0

        edit_expid = request.GET.get('edit_exp')
        if edit_expid:
            edit_expid = int(edit_expid)
        else:
            edit_expid = 0

        type = request.GET.get('type')
        edit_exp=None
        if type=="intern":
            edit_exp=experience_internship.objects.filter(userid=userobj,valid=3,id=edit_expid).first()
            print edit_exp,"dddd"
            if edit_exp is None: #someone is not authentic to open this so
                return HttpResponseRedirect('/home/')
        elif type=="job":
            edit_exp = experience_placement.objects.filter(userid=userobj,valid=3, id=edit_expid).first()
            if edit_exp is None:  # someone is not authentic to open this
                return HttpResponseRedirect('/home/')


        print "new_exp",new_exp

        if (saved_intern_exp or saved_job_exp) and new_exp != 1 and edit_expid==0:
            Context['page_name'] = "Saved Experiences"
            return render_to_response(
                'saved_experiences.html', Context, context_instance=RequestContext(request)
            )

        #Else send everything to the form
        Context.update({'edit_exp':edit_exp,'type':type})
        Context['page_name']="Write your experience"

        ''' END '''
        return render_to_response(
        'experienceform.html',Context,context_instance=RequestContext(request)
        )
  else:
        cannot_contribute=1
        return HttpResponseRedirect('/home/?cannot_contribute='+str(cannot_contribute))


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def experience_of_intern(request,expid):
    experience=experience_internship.objects.filter(id=expid).first()
    #print experience.company_id
    company=Company_Department_Relation.objects.filter(id=experience.cdr_id.id).first().company_id

    page_name = experience.cdr_id.company_id.display_name
    exp_type=" Internship interview Experience"

    list=[] # round1_text. round2_text,etc
    for attr, value in experience_internship().__dict__.iteritems():
        if attr.endswith("text_id"):
            attr=str(attr[:-3]) # remove the _id from last : round1_text_id -> round1_text
            list.append(attr)
    list.sort()
    #print list

    Context={'list':list,'company':company,'experience':experience}
    Context.update({'page_name':page_name,'exp_type':exp_type})

    Context.update(headerdb(request))
    Context.update(csrf(request))

    return render_to_response(
    'experienceofintern.html',Context,context_instance=RequestContext(request)
    )


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def experience_of_placement(request,expid):
    experience=experience_placement.objects.filter(id=expid).first()
    company=Company_Department_Relation.objects.filter(id=experience.cdr_id.id).first().company_id

    page_name = experience.cdr_id.company_id.display_name
    exp_type=" Job interview Experience"

    list=[] # round1_text. round2_text,etc
    for attr, value in experience_placement().__dict__.iteritems():
        if attr.endswith("text_id"):
            attr=str(attr[:-3]) # remove the _id from last : round1_text_id -> round1_text
            list.append(attr)
    list.sort()
    #print list

    Context={'list':list,'company':company,'experience':experience}
    Context.update({'page_name':page_name,'exp_type':exp_type})

    Context.update(headerdb(request))
    Context.update(csrf(request))

    return render_to_response(
    'experienceofintern.html',Context,context_instance=RequestContext(request)
    )


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def dept_selected(request,deptid):

    print type(deptid)
    deptid=int(deptid)
    deptobj = Department.objects.get(id=deptid)

    interns_cdr=Company_Department_Relation.objects.filter(deptid=deptid,intern_valid=1)
    interns=[]
    for i in interns_cdr:
        interns=interns+list(company_table.objects.filter(id=i.company_id.id,valid=1))
    interns=list(set(interns))

    jobs_cdr=list(set(Company_Department_Relation.objects.filter(deptid=deptid,job_valid=1)))
    jobs=[]
    for i in jobs_cdr:
        jobs=jobs+list(company_table.objects.filter(id=i.company_id.id,valid=1))
    jobs=list(set(jobs))


    interns_cdr=Company_Department_Relation.objects.filter(deptid=deptid,intern_valid=1)
    dept_exp_intern_list=[]
    for i in interns_cdr:
        dept_exp_intern_list=dept_exp_intern_list+list(experience_internship.objects.filter(valid=1,cdr_id=i.id))

    jobs_cdr=list(set(Company_Department_Relation.objects.filter(deptid=deptid,job_valid=1)))
    dept_exp_job_list=[]
    for i in jobs_cdr:
        dept_exp_job_list=dept_exp_job_list+list(experience_placement.objects.filter(valid=1,cdr_id=i.id))

    #Sorting List of objects with object attribute
    recentjob = sorted(jobs, key=lambda x: x.recentdate, reverse=True)
    recentinterns = sorted(interns, key=lambda x: x.recentdate, reverse=True)

    #Sort experiences
    dept_exp_intern_list = sorted(dept_exp_intern_list, key=lambda x: x.timestamp, reverse=True)
    dept_exp_job_list = sorted(dept_exp_job_list, key=lambda x: x.timestamp, reverse=True)

    ''' Pagination '''
    intern_paginator = Paginator(interns,10)

    internpage = request.GET.get('internpage')
    try:
        interns = intern_paginator.page(internpage)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        interns = intern_paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        interns = intern_paginator.page(intern_paginator.num_pages)
    ''' End of pagination '''

    ''' Pagination '''
    job_paginator = Paginator(jobs,10)

    jobpage = request.GET.get('jobpage')
    try:
        jobs = job_paginator.page(jobpage)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        jobs = job_paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        jobs = job_paginator.page(job_paginator.num_pages)
    ''' End of pagination '''

    ''' Pagination '''
    job_exp_paginator = Paginator(dept_exp_job_list,10)

    job_exp_page = request.GET.get('job_exp_page')
    try:
        dept_exp_job_list = job_exp_paginator.page(job_exp_page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        dept_exp_job_list = job_exp_paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        dept_exp_job_list = job_exp_paginator.page(job_exp_paginator.num_pages)
    ''' End of pagination '''

    ''' Pagination '''
    intern_exp_paginator = Paginator(dept_exp_intern_list,10)

    intern_exp_page = request.GET.get('intern_exp_page')
    try:
        dept_exp_intern_list = intern_exp_paginator.page(intern_exp_page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        dept_exp_intern_list = intern_exp_paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        dept_exp_intern_list = intern_exp_paginator.page(intern_exp_paginator.num_pages)
    ''' End of pagination '''


    page_name = deptobj.short_name
    Context={'page_name':page_name,'recentjob':recentjob[:5],'recentinterns':recentinterns[:5],'deptobj':deptobj,'interns':interns,'jobs':jobs,'dept_exp_intern_list':dept_exp_intern_list,'dept_exp_job_list':dept_exp_job_list
		}
    Context.update(csrf(request))
    Context.update(headerdb(request))

    return render_to_response(
      'dept_home.html',Context,context_instance=RequestContext(request))


@csrf_protect
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def edit_profile(request,clg_id):
    if request.method == "POST":
        clg_id = base64.urlsafe_b64decode(clg_id.encode("ascii"))
        print clg_id
        fname=request.POST.get('fname','')
        lname = request.POST.get('lname','')
        tel1 = request.POST.get('telephone1','')
        tel2 = request.POST.get('telephone2','')
        oldpassword = request.POST.get('oldpassword','')
        pass1 = request.POST.get('password1','')
        pass2 = request.POST.get('password2','')

        person_obj = Personinformation.objects.get(clg_id=request.session['clg_id'])

        login_obj = ForLogin.objects.get(clg_id=person_obj)

        #server
        err_msg=server_validations.isvalid_editprofile(fname,lname,tel1,tel2,oldpassword,pass1,pass2)

        flag=0
        if len(err_msg)!=0:
            flag=1
        if len(oldpassword)>8:
            if not (check_password(oldpassword,login_obj.password)):
                err_msg.append("old password entered not valid.Try again.")
                flag=2
        print err_msg
        if flag!=0:
            person_obj.firstname=fname
            person_obj.lastname=lname
            person_obj.telephone1=tel1
            person_obj.telephone2=tel2
            deptname = Department.objects.get(id=person_obj.deptid).display_name

            Context={'err_msg':err_msg,'person_obj':person_obj,'deptname':deptname}
            Context.update(csrf(request))
            Context.update(headerdb(request))
            return render_to_response(
        'edit_profile.html',Context,context_instance=RequestContext(request)
        )



        if check_password(oldpassword,login_obj.password):
            login_obj.password = make_password(pass1)
            login_obj.save()
            print "Password successfully changed"
        else :
            print "oops wrong old passsword"



        person_obj.firstname = fname
        person_obj.lastname = lname
        person_obj.telephone1= tel1
        person_obj.telephone2= tel2
        person_obj.save()


        return HttpResponseRedirect('/home/')
    #get clg_id from session.

    clg_id = base64.urlsafe_b64decode(clg_id.encode("ascii"))
    print clg_id
    person_obj = Personinformation.objects.get(clg_id=clg_id)
    login_obj = ForLogin.objects.get(clg_id=person_obj)
    jobexp_obj = experience_placement.objects.filter(userid=person_obj)
    internexp_obj = experience_internship.objects.filter(userid=person_obj)

    deptname = Department.objects.get(id=person_obj.deptid).display_name
    print deptname

    Context = {}
    Context = { 'page_name':"Edit Your Profile",'deptname':deptname, 'person_obj' : person_obj , 'login_obj': login_obj , 'jobexp_obj' : jobexp_obj , 'internexp_obj' : internexp_obj }
    Context.update(csrf(request))
    Context.update(headerdb(request))

    if 'clg_id' in request.session :
	    return render_to_response(
	      'edit_profile.html',Context,context_instance=RequestContext(request)
	      )
    else:
	return HttpResponseRedirect('/home/')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def admin_request(request):
    if request.method == "POST":
        submit =  request.POST.get('button','')
        print submit

        submit = submit.split('|')
        requestid = submit[1]
        submit_type = submit[0]

        print requestid,submit_type
        request_obj = Requests.objects.get(id=requestid)

        if submit_type == "Accept":
            print "Accept"

            name = request.POST.get('company_name','')
            short = request.POST.get('short_name','')
            long = request.POST.get('long_name','')
            display = request.POST.get('display_name','')
            session = request.POST.get('session','')
            startdate = request.POST.get('startdate','')
            recentdate = request.POST.get('recentdate','')
            print startdate,recentdate


            # Update company table
            compobj = company_table.objects.get(id = request_obj.company_id.id)
            compobj.company_name = name
            compobj.short_name = short
            compobj.long_name = long
            compobj.display_name = display
            compobj.startdate = startdate
            compobj.recentdate = recentdate
            compobj.valid =1

            #return HttpResponseRedirect('/home/admin_request/')

             #Update request table
            request_obj.status = 1
            request_obj.save()

            #Job exp.
            if request_obj.job_exp_id is not None :
                compobj.job_exp_count = 0 # We will update it once tnp head approves it
                compobj.company_job_valid = 1
                userobj = request_obj.job_exp_id.userid
            elif request_obj.intern_exp_id is not None :
                compobj.intern_exp_count = 0 # We will update it once studentportal head approves it
                compobj.company_intern_valid = 1
                userobj = request_obj.intern_exp_id.userid

            compobj.save()

            #Creation of CDR object
            deptobj = Department.objects.get(id = userobj.deptid)
            cdrobj = Company_Department_Relation(deptid=deptobj,company_id=compobj,session=request_obj.session)
            if request_obj.job_exp_id is not None :
                cdrobj.intern_valid = 1

            elif request_obj.intern_exp_id is not None :
                cdrobj.job_valid = 1

            cdrobj.save()


            #Update exp table
            if request_obj.job_exp_id is not None :
                expobj = request_obj.job_exp_id
            elif request_obj.intern_exp_id is not None :
                expobj = request_obj.intern_exp_id

            expobj.cdr_id= cdrobj
            expobj.valid = 0
            expobj.save()


        elif submit_type == "List":
            print "List"
            dept_checked = request.POST.getlist('dept','')
            _type = request.POST.getlist('type','')
            comp_obj = request.POST.get('company_name','')
            session = request.POST.get('session','')

            print "dept",dept_checked
            print _type,session

            #return HttpResponseRedirect('/home/admin_request/')

            #Invalidate the requested company name from company table-as the company already exists.
            compobj = request_obj.company_id
            '''compobj.valid = -1            
            compobj.save()
            '''
            #Update request table - request accepted
            request_obj.status = 1
            request_obj.save()

            print "dept",dept_checked

            #If the triplet+type already exist then Add the cdrid to the  object.
            #Else create a CDR object and then add the cdrid to the experience object.
            for dept in dept_checked:
                dept_obj=Department.objects.filter(id=dept).first()
                cdrobj = Company_Department_Relation.objects.filter(deptid=dept_obj,company_id=comp_obj,session=session).first()
                print "smile please"
                if cdrobj is None:
                     #Create a CDR object with the given department and session and type
                     cdrobj = Company_Department_Relation(deptid=dept_obj,company_id=compobj,session=session)
                     cdrobj.save()


                #Update CDR and company table
                if request_obj.job_exp_id is not None :
                    cdrobj.job_valid = 1
                    cdrobj.save()

                    expobj = request_obj.job_exp_id
                    if expobj.userid.deptid == dept_obj.id:
                        user_cdrobj = cdrobj

                    compobj=cdrobj.company_id
                    compobj.job_valid=1
                    compobj.save()
                    print "\n Job"
                elif request_obj.intern_exp_id is not None :
                    cdrobj.intern_valid = 1
                    cdrobj.save()

                    expobj = request_obj.intern_exp_id
                    if expobj.userid.deptid == dept_obj.id:
                        user_cdrobj = cdrobj

                    compobj=cdrobj.company_id
                    compobj.intern_valid=1
                    compobj.save()
                    print "\n Intern"



                #For all the placement types checked
                for t in _type:
                    if int(t)==0: #internvalid
                        cdrobj.intern_valid=1
                        cdrobj.company_id.intern_valid=1
			print "Intern type",t
                    else: #jobvalid
                        cdrobj.job_valid=1
                        cdrobj.company_id.job_valid=1
               		print "Job Type",t

                cdrobj.save()


            #Update exp table
            if request_obj.job_exp_id is not None :
                expobj = request_obj.job_exp_id
            elif request_obj.intern_exp_id is not None :
                expobj = request_obj.intern_exp_id

            expobj.cdr_id = user_cdrobj
            expobj.valid = 0
            expobj.save()
            return HttpResponseRedirect('/home/admin_request/')
        elif submit_type == "Reject":
            print "Reject"
            # Update request rejected
            request_obj.status = -1
            request_obj.save()

            if request_obj.job_exp_id is not None :
                    expobj = request_obj.job_exp_id
                    print "\n Job"
            elif request_obj.intern_exp_id is not None :
                    expobj = request_obj.intern_exp_id
                    print "\n Intern"
            #Update exp as rejected
            expobj.valid=-1
            expobj.save()

            #Update company reject
            compobj = request_obj.company_id
            compobj.valid = -1
            compobj.save()

        return HttpResponseRedirect('/home/admin_request/')
        #print request.POST.get('b2','')

    #GET request
    Context = {}
    Context.update(csrf(request))
    Context.update(headerdb(request))

    requestobj_list = Requests.objects.filter( (Q(intern_exp_id__cdr_id__isnull=True) & Q(intern_exp_id__valid=0)) | (Q(job_exp_id__cdr_id__isnull=True) & Q(job_exp_id__valid=0) ))  #.filter(intern_exp_id__valid=0)
    #print "\n This",request_obj
    #request_list=list(request_obj)
    intern_req_list = []
    job_req_list = []

    for i in requestobj_list:
        if i.intern_exp_id :
            intern_req_list.append(i)
        else:
            job_req_list.append(i)

    intern_req_list=sorted(intern_req_list, key=lambda x: x.intern_exp_id.timestamp, reverse=True)
    job_req_list=sorted(job_req_list, key=lambda x: x.job_exp_id.timestamp, reverse=True)

    print intern_req_list
    print job_req_list

    all_companies = company_table.objects.filter(valid=1) #Only those companies whose request is accepted from the higher authoriities.
    dept_obj = Department.objects.all()

    Context.update({'page_name':'Accept Company Requests','intern_req_list':intern_req_list,'job_req_list':job_req_list,'all_companies':all_companies,'dept_obj':dept_obj})

    return render_to_response(
      'admin_request.html',Context,context_instance=RequestContext(request)
      )

def sendemail(expobj,flag,view_link,link): #flag=1 accept,flag=0 reject    
	clg_id = expobj.userid.clg_id
	emailobj = Personinformation.objects.filter(clg_id=clg_id).first()
	email = emailobj.email

	if flag:
		html_msg = loader.render_to_string('contribute_success_email.html',{'name':expobj.userid.firstname,'link':link,'view_link':view_link })
	else:
		html_msg = loader.render_to_string('contribute_reject_email.html',{'name':expobj.userid.firstname,'link':link })

       	send_mail('Response from Student Portal',"Hello", FROM_EMAIL, [email],html_message=html_msg)

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def exp_request(request):
    if request.method == "POST":
        submit =  request.POST.get('button','')
        print submit

        submit = submit.split('|')
        expid = submit[1]
        submit_type = submit[0]
        job_type = submit[2]

        print expid,submit_type
        link = request.META['HTTP_HOST']
	view_link=None

        if submit_type == "Accept":
            print "Accept"
	    expobj=None
            if job_type == "intern": #intern
                expobj = experience_internship.objects.get(id=expid)
                expobj.valid = 1
                expobj.save()

                compobj = expobj.cdr_id.company_id
                compobj.intern_exp_count += 1
                compobj.company_intern_valid=1
                compobj.save()

                cdrobj=expobj.cdr_id
                cdrobj.intern_valid=1
                cdrobj.save()

		view_link=link+"/exp_intern/"+str(expobj.id)

            else : #JOb
                expobj = experience_placement.objects.get(id=expid)
                expobj.valid = 1
                expobj.save()

                compobj = expobj.cdr_id.company_id
                compobj.job_exp_count += 1
                compobj.company_job_valid=1
                compobj.save()

                cdrobj=expobj.cdr_id
                cdrobj.job_valid=1
                cdrobj.save()

		view_link=link+"/exp_placed/"+str(expobj.id)
	    link+="/home"
	    sendemail(expobj,1,view_link,link)
        elif submit_type == "Reject" :
            print "Reject"
            if job_type == "intern": #Intern
                expobj = experience_internship.objects.get(id=expid)
                expobj.valid = -1
                expobj.save()
            else : #Job
                expobj = experience_placement.objects.get(id=expid)
                expobj.valid = -1
                expobj.save()
            link+="/home"
      	    sendemail(expobj,0,view_link,link)

        return HttpResponseRedirect('/home/exp_request/')

    Context = {}
    Context.update(csrf(request))
    Context.update(headerdb(request))

    personobj=Personinformation.objects.filter(clg_id=request.session['clg_id']).first()
    deptid=personobj.deptid

    #So that no other with the URL could see the page
    if personobj.roleid.role_id != 2 : #TNP Head
        print "Not okay"
        return HttpResponseRedirect('/home/')

    print "deptid",deptid
    #userid.deptid=deptid

    #Currently TNP Head of CSE is accepting everyones request. Add this to the filter later : 'userid__deptid=deptid'
    intern_exp_obj = experience_internship.objects.filter(valid=0).exclude(cdr_id__isnull=True)



    intern_exp_obj=sorted(intern_exp_obj, key=lambda x: x.timestamp, reverse=True)
    #print intern_exp_obj

    Context['intern_exp_obj_request']=intern_exp_obj

    #Currently TNP Head of CSE is accepting everyones request. Add this to the filter later : 'userid__deptid=deptid'
    job_exp_obj = experience_placement.objects.filter(valid=0).exclude(cdr_id__isnull=True)



    job_exp_obj=sorted(job_exp_obj, key=lambda x: x.timestamp, reverse=True)
    #print job_exp_obj

    Context['job_exp_obj_request']=job_exp_obj

    Context['page_name']="Accept Experience Requests | "+Department.objects.filter(id=deptid).first().short_name

    ''' Pagination 
    paginator = Paginator(intern_exp_obj,5)
    
    page = request.GET.get('page')
    try:
        intern_exp_obj = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        intern_exp_obj = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        intern_exp_obj = paginator.page(paginator.num_pages)
     End of pagination '''


    return render_to_response(
      'exp_request.html',Context,context_instance=RequestContext(request)
      )



#Done by rathi hereforth 

@csrf_protect
def add_Admin(request):
   if request.method == "POST":
       user_id = request.POST['user_id']
       user = Personinformation.objects.get(clg_id=user_id)
       # toroleid_tnp = Roles.objects.get(short_name='TNP Head')
       toroleid_Admin = Roles.objects.get(short_name='Admin')
       toroleid_student = Roles.objects.get(short_name='Student')

       if user.roleid.short_name == 'Admin':
           user.roleid = toroleid_student
           user.save()
           # data.update({'role_id': user.roleid.short_name})
       else:
           user.roleid = toroleid_Admin
           user.save()
       # data.update({'role_id': user.roleid.short_name})
       # args = {}
       # args.update(headerdb(request))
       # args.update(csrf(request))
       # return render(request,'add_tnp_head.html', args)
   roleid_Admin = Roles.objects.get(short_name='Admin').pk
   admin_list = Personinformation.objects.filter(roleid=roleid_Admin)
   context = {'page_name': "Admin details", 'admin_list': admin_list}
   context.update(csrf(request))
   context.update(headerdb(request))
   return render(request, "add_admin.html", context)


@csrf_protect
def add_tnp_head(request):
   if request.method == "POST":
       user_id = request.POST['user_id']
       print('user_id'+user_id)
       user = Personinformation.objects.get(clg_id=user_id)
       toroleid_tnp = Roles.objects.get(short_name='TNP Head')
       toroleid_student = Roles.objects.get(short_name='Student')

       if user.roleid.short_name == 'TNP Head':
           user.roleid = toroleid_student
           user.save()
           # data.update({'role_id': user.roleid.short_name})
       else:
           user.roleid = toroleid_tnp
           user.save()
   roleid_TNPHead = Roles.objects.get(short_name='TNP Head').pk
   TNPHead_list = Personinformation.objects.filter(roleid=roleid_TNPHead)
   Context = {'page_name':"TNP Head details",'TNPHead_list':TNPHead_list}
   Context.update(csrf(request))
   Context.update(headerdb(request))
   print(TNPHead_list)
   return render(request, "add_tnp_head.html", Context)


def tnp_head_admin_details(request, user_id):
   try:
       user = Personinformation.objects.get(clg_id=user_id)

       data = dict()
       data.update({'isvalid': 'True', 'fname': user.firstname, 'lname': user.lastname, 'roll_no': user.roll_no})
       dept_name = Department.objects.get(pk=user.deptid).long_name
       data.update({'dept_name': dept_name, 'role_id': user.roleid.short_name})

       # print(data)
       # new1={'new':'hi'}
       # dict={'data':data,'new1':new1}
       # return HttpResponse(json.dumps([data,new1], cls=DjangoJSONEncoder), content_type="application/json")
       return HttpResponse(json.dumps(data, cls=DjangoJSONEncoder), content_type="application/json")

   except ObjectDoesNotExist:
       data = dict()
       data.update({'isvalid': 'False'})
       return HttpResponse(json.dumps(data, cls=DjangoJSONEncoder), content_type="application/json")

#rathis work end

def redirect_home(request):
	return HttpResponseRedirect('/home/')
