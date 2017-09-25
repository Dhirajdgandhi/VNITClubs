from django.contrib import admin
from models import company_table,Personinformation,ForLogin,Department,experience_placement,experience_internship,Requests,Company_Department_Relation,Roles,ForgotPassKeys
from models import Difficulty_type,InterviewRound_type,InterviewRound_details,Profile_type,Session
# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
	list_display = ['company_name', 'id', 'startdate', 'recentdate']
	class Meta:
		model = company_table

admin.site.register(company_table, CompanyAdmin)
admin.site.register(Personinformation)
admin.site.register(ForLogin)
admin.site.register(Department)
admin.site.register(experience_placement)
admin.site.register(experience_internship)
admin.site.register(Requests)
admin.site.register(Company_Department_Relation)
admin.site.register(Roles)
admin.site.register(Difficulty_type)
admin.site.register(InterviewRound_type)
admin.site.register(InterviewRound_details)
admin.site.register(Profile_type)
admin.site.register(Session)
admin.site.register(ForgotPassKeys)
