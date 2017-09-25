from django.db import models
# from django.forms import ModelForm
import datetime
# import django.utils.timezone

# from encrypted_id.models import EncryptedIDModel


# class Foo(EncryptedIDModel):
# text = models.TextField()

class Roles(models.Model):
    role_id = models.AutoField(primary_key=True, null=False)
    short_name = models.TextField(max_length=45, null=True)
    long_name = models.TextField(max_length=45, null=True)
    display_name = models.TextField(max_length=45, null=True)

    def __unicode__(self):
        return self.short_name


class Department(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    # name=models.CharField(max_length=75,null=True) #Computer Science And Engg.

    # deptid = models.CharField(max_length=5,null=True) #CSE
    # ''' deptid replaced by shortname '''
    short_name = models.TextField(max_length=45, null=True)
    long_name = models.TextField(max_length=45, null=True)
    display_name = models.TextField(max_length=45, null=True)

    program = models.TextField(max_length=45, null=True)  # Structural Enginnering
    degree_level = models.TextField(max_length=45, null=True)  # MTech

    def __unicode__(self):
        return self.short_name

    def get_absolute_url(self):
        return "/dept_home/%i/" % self.id


class Personinformation(models.Model):
    roleid = models.ForeignKey(Roles, default=1, null=False)  # 1- Student
    email = models.EmailField(max_length=100, null=False)  # ddgandhi.96@gmail.com
    firstname = models.TextField(max_length=45, null=True)  # Dhiraj
    lastname = models.TextField(max_length=45, null=True)  # Gandhi
    telephone1 = models.CharField(max_length=15, null=True)  # 8655022884
    telephone2 = models.CharField(max_length=15, null=True)
    clg_id = models.IntegerField(max_length=5, primary_key=True)
    deptid = models.IntegerField(max_length=5)  # CSE Mtech 2016 - Storing the id
    roll_no = models.TextField(max_length=10, null=True)  # BT13CSE033
    createdondate = models.DateField(null=False, default=datetime.date.today())
    is_active = models.IntegerField(default=1, null=False)

    class Meta:
        managed = True

    def __unicode__(self):
        return self.firstname + " " + self.lastname

# ''' Note :- Kindly see if we need to alter the login table as we are now having Multiple roles ,so what will the profs clg_id be? '''


class ForLogin(models.Model):
    clg_id = models.ForeignKey(Personinformation)  #
    password = models.CharField(max_length=500, null=True)  # dhirajdg

    class Meta:
        managed = True

    def __unicode__(self):
        return self.clg_id.firstname + " " + self.clg_id.lastname


class company_table(models.Model):
    # company_id=models.IntegerField(primary_key=True,null=False)
    id = models.AutoField(primary_key=True, null=False)
    company_name = models.TextField(null=True)

    short_name = models.TextField(max_length=45, null=True)
    long_name = models.TextField(max_length=45, null=True)
    display_name = models.TextField(max_length=45, null=True)

    intern_exp_count = models.IntegerField(default=1)
    job_exp_count = models.IntegerField(default=1)

    company_intern_valid = models.IntegerField(default=0)
    company_job_valid = models.IntegerField(default=0)
    '''
    dept1_applicable=models.IntegerField(default=0) #CSE
    dept2_applicable=models.IntegerField(default=0) #CHEM
    dept3_applicable=models.IntegerField(default=0)    #CIV
    dept4_applicable=models.IntegerField(default=0) #ECE
    dept5_applicable=models.IntegerField(default=0) #EEE
    dept6_applicable=models.IntegerField(default=0) #MECH
    dept7_applicable=models.IntegerField(default=0) #META
    dept8_applicable=models.IntegerField(default=0) #MIN
    dept9_applicable=models.IntegerField(default=0) #ARCHI

    deptid = models.ForeignKey(Department)
    '''
    startdate = models.DateField(null=False)  # Gives the date when the company first came to our campus.
    recentdate = models.DateField(default=datetime.date.today(),
                                  null=False)  # Gives the recent date of visit to the campus
    valid = models.IntegerField(default=0)  # Is the request accepted by higher authorities?

    # To be added in the END
    ''' image_logo = IMAGE Field (Image Logo of the company )
    comapny_website = URL field ( The website url of the company)
    description = Text Field (Short description about the company )     
    '''

    def get_absolute_url(self):
        return "/company_select/%i/" % self.id

    def __unicode__(self):
        return self.company_name

# '''class Meta:
# 		managed = True
# '''


class Company_Department_Relation(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    deptid = models.ForeignKey(Department)
    company_id = models.ForeignKey(company_table)
    session = models.CharField(max_length=20, null=True)
    intern_valid = models.IntegerField(default=0)  # Whether valid for that session
    job_valid = models.IntegerField(default=0)  # Whether valid for that session

    def __unicode__(self):
        return self.deptid.short_name + "-" + self.company_id.company_name


class Session(models.Model):  # 2016-2017
    id = models.AutoField(primary_key=True, null=False)
    display_name = models.TextField()
    description = models.TextField()

    def __unicode__(self):
        return self.display_name


class Profile_type(models.Model):  # Sofware Analyst
    id = models.AutoField(primary_key=True, null=False)
    display_name = models.TextField()
    description = models.TextField()

    def __unicode__(self):
        return self.display_name


class Difficulty_type(models.Model):  # Easy
    id = models.AutoField(primary_key=True, null=False)
    display_name = models.TextField()
    description = models.TextField()

    def __unicode__(self):
        return self.display_name


class InterviewRound_type(models.Model):  # HR
    id = models.AutoField(primary_key=True, null=False)
    display_name = models.TextField()
    description = models.TextField()

    def __unicode__(self):
        return self.display_name


class InterviewRound_details(models.Model):  # ALl details of an exp
    id = models.AutoField(primary_key=True, null=False)
    time = models.IntegerField(default=0)
    difficulty = models.ForeignKey(Difficulty_type)
    round_type = models.ForeignKey(InterviewRound_type)
    description = models.TextField(null=True)

    def __unicode__(self):
        return self.round_type.display_name + "-" + self.difficulty.display_name


class experience_placement(models.Model):
    # experience_num = models.IntegerField(primary_key=True,null=False)
    id = models.AutoField(primary_key=True, null=False)

    cdr_id = models.ForeignKey(Company_Department_Relation, null=True)
    # company_id=models.ForeignKey(company_table)

    profile = models.ForeignKey(Profile_type, null=True)
    criteria = models.CharField(max_length=500, null=True)
    onoffcampus = models.IntegerField(default=1, max_length=5, null=False)
    package = models.FloatField(null=True)
    cgpa = models.FloatField(null=True)
    userid = models.ForeignKey(Personinformation)
    num_of_rounds = models.IntegerField(default=0)
    round1_text = models.ForeignKey(InterviewRound_details, null=True, blank=True, related_name="%(class)s_round1")
    round2_text = models.ForeignKey(InterviewRound_details, null=True, blank=True, related_name="%(class)s_round2")
    round3_text = models.ForeignKey(InterviewRound_details, null=True, blank=True, related_name="%(class)s_round3")
    round4_text = models.ForeignKey(InterviewRound_details, null=True, blank=True, related_name="%(class)s_round4")
    round5_text = models.ForeignKey(InterviewRound_details, null=True, blank=True, related_name="%(class)s_round5")
    round6_text = models.ForeignKey(InterviewRound_details, null=True, blank=True, related_name="%(class)s_round6")

    other_comments = models.TextField(default="")

    timestamp = models.DateTimeField(default=datetime.datetime.now(), null=False)  # When was this experience shared.
    valid = models.IntegerField(default=0)
    selected = models.IntegerField(default=1)

    def get_absolute_url(self):
        return "/exp_placed/%i/" % self.id

    def __unicode__(self):
	try:
        	return self.cdr_id.company_id.company_name + "-" + self.userid.firstname + " " + self.userid.lastname
	except AttributeError:
		return self.userid.firstname + " " + self.userid.lastname + " (Pending)"


class experience_internship(models.Model):
    # experience_num=models.AutoField(primary_key=True,null=False)
    id = models.AutoField(primary_key=True, null=False)

    cdr_id = models.ForeignKey(Company_Department_Relation, null=True)
    # company_id=models.ForeignKey(company_table)

    profile = models.ForeignKey(Profile_type, null=True)
    criteria = models.CharField(max_length=500, null=True)
    onoffcampus = models.IntegerField(default=1, max_length=5, null=False)
    package = models.FloatField(null=True)
    cgpa = models.FloatField(null=True)
    userid = models.ForeignKey(Personinformation)
    num_of_rounds = models.IntegerField(default=0)
    round1_text = models.ForeignKey(InterviewRound_details, null=True, blank=True, related_name="%(class)s_round1")
    round2_text = models.ForeignKey(InterviewRound_details, null=True, blank=True, related_name="%(class)s_round2")
    round3_text = models.ForeignKey(InterviewRound_details, null=True, blank=True, related_name="%(class)s_round3")
    round4_text = models.ForeignKey(InterviewRound_details, null=True, blank=True, related_name="%(class)s_round4")
    round5_text = models.ForeignKey(InterviewRound_details, null=True, blank=True, related_name="%(class)s_round5")
    round6_text = models.ForeignKey(InterviewRound_details, null=True, blank=True, related_name="%(class)s_round6")

    other_comments = models.TextField(default="")

    timestamp = models.DateTimeField(default=datetime.datetime.now(), null=False)  # When was this experience shared.
    valid = models.IntegerField(default=0)
    selected = models.IntegerField(default=1)

    def get_absolute_url(self):
        return "/exp_intern/%i/" % self.id

    def __unicode__(self):
	try:
        	return self.cdr_id.company_id.company_name + "-" + self.userid.firstname + " " + self.userid.lastname
	except AttributeError:
		return self.userid.firstname + " " + self.userid.lastname + " (Pending/Saved)"

#     '''def __unicode__(self):
#         return unicode(self.round1_text)
#     def __getitem__(self,key_name):
#         if (key_name=="round1_text"):
#             self.round1_text
#         else:
#             self[key_name]
#     '''
# ''' Requests for a company whose experience is already mentioned by the user '''


class Requests(models.Model):
    # id=models.AutoField(primary_key=True,null=False)
    job_exp_id = models.ForeignKey(experience_placement, null=True)
    intern_exp_id = models.ForeignKey(experience_internship, null=True)
    company_id = models.ForeignKey(company_table, null=True)
    session = models.TextField(null=True)
    status = models.IntegerField(default=0)  # 0- pending , 1- accepted , 2- declined/rejected

    def __unicode__(self):
	try:
		try:
		    company_name = self.job_exp_id.cdr_id.company_id.company_name
		    user_name = self.job_exp_id.userid.firstname + " " + self.job_exp_id.userid.lastname
		    return company_name + "-" + user_name + " (P)"
		except AttributeError:
		    company_name = self.intern_exp_id.cdr_id.company_id.company_name
		    user_name = self.intern_exp_id.userid.firstname + " " + self.intern_exp_id.userid.lastname
		    return company_name + "-" + user_name + " (I)"
	except AttributeError:
		company_name = "New Company"
		try:
			user_name = self.job_exp_id.userid.firstname + " " + self.job_exp_id.userid.lastname
		except AttributeError:
			user_name = self.intern_exp_id.userid.firstname + " " + self.intern_exp_id.userid.lastname
		return company_name + "-" + user_name + " (P)"


class ForgotPassKeys(models.Model):
    key = models.CharField(max_length=20, null=True)
    user = models.ForeignKey(Personinformation, null=True)
    is_valid = models.BooleanField(default=True)
    timestamp = models.DateTimeField(default=datetime.datetime.now(), null=False)

    def __unicode__(self):
        return self.user.firstname + ' ' + self.user.lastname

# For comments on experience
# '''
# class comments(models.Model):
#     id = models.AutoField(primary_key=True,null=False)
#     intern_exp_id = models.ForeignKey(experience_internship,null=True)
#     job_exp_id = models.ForeignKey(experience_placement,null=True)
#     comment = models.TextField(null=True) # Thank you for sharing the experience
#     by = models.ForeignKey(Personinformation,null=False) #clg_id of user
#     replyto = models.ForeignKey(comments,null=True) # on which comment
# '''
