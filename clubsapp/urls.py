from django.conf.urls import url

urlpatterns = [
    url(r'^$' , 'clubsapp.views.clubs' ),
    url(r'^(?P<clubName>.*)/$', 'clubsapp.views.clubHome'),
]