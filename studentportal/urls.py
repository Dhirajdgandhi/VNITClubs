"""StudentPortal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import (  handler404, handler500 )
handler404 = 'portalapp.views.page_not_found'
handler500 = 'portalapp.views.server_error'



admin.autodiscover()

urlpatterns = [
    url(r'^thisisouradminpage/', include(admin.site.urls)),
    # url(r'^register/$', 'portalapp.views.register'),
    url(r'^success/$', 'portalapp.views.success'),
    url(r'^login/$', 'portalapp.views.login'),
    url(r'^forgotpass/$', 'portalapp.views.forgotpass'),
    url(r'^resetpass/(?P<fkey>.*)/$', 'portalapp.views.resetpass'),
    url(r'^home/$', 'portalapp.views.homepage'),
    url(r'^$', 'portalapp.views.redirect_home'),
    url(r'^edit_profile/(?P<clg_id>.*)/$','portalapp.views.edit_profile'),
    url(r'^logout/$', 'portalapp.views.logout'),
    url(r'^home/contribute/$', 'portalapp.views.fill_experience'),
    url(r'^home/admin_request/$', 'portalapp.views.admin_request'),
    url(r'^home/exp_request/$', 'portalapp.views.exp_request'),
    url(r'dept_home/(?P<deptid>[1-9])/$', 'portalapp.views.dept_selected'),
    url(r'^exp_placed/(?P<expid>[0-9]+)/$', 'portalapp.views.experience_of_placement'),
    url(r'^exp_intern/(?P<expid>[0-9]+)/$', 'portalapp.views.experience_of_intern'),
    url(r'^home/company_select/(?P<comp_id>[0-9]+)/job/$','portalapp.views.company_placements'),
    url(r'^home/company_select/(?P<comp_id>[0-9]+)/intern/$','portalapp.views.company_internships'), 
    
    url(r'^home/add_tnp_head/$','portalapp.views.add_tnp_head'),
	 url(r'^home/add_tnp_head/(?P<user_id>[0-9]+)/$','portalapp.views.tnp_head_admin_details'),
	 url(r'^home/add_admin/$','portalapp.views.add_Admin'),
	 url(r'^home/add_admin/(?P<user_id>[0-9]+)/$','portalapp.views.tnp_head_admin_details'),
	 
    url(r'^login/(?P<comp_id>[0-9]+)/intern/$','portalapp.views.login'),
    url(r'^register/(?P<comp_id>[0-9]+)/intern/$','portalapp.views.register'),
    url(r'^forgotpass/(?P<comp_id>[0-9]+)/intern/$','portalapp.views.forgotpass'),
		
	 url(r'^home/aboutus/$','portalapp.views.aboutus'),
    url ( r'^clubs/$' , 'clubsapp.views.page_not_found' ) ,
]

'''  

   
       url(r'^company/(?P<compid>[0-9]+)/$','portalapp.views.company'),

   
   
url(r'^dept/(?P<deptid>[1-9])/$','portalapp.views.dept_selected'),
  url(r'^company_select/(?P<compid>[0-9]+)/intern/$','portalapp.views.company_internships'),
    url(r'^company_select/(?P<compid>[0-9]+)/job/$','portalapp.views.company_placements'),
       
'''
