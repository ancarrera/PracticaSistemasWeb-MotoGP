from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import *
from django.contrib.auth.views import logout
from appMotoGP.views import *
from appMotoGP.form import *


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'motoGP.views.home', name='home'),
    # url(r'^motoGP/', include('motoGP.foo.urls')),
    #url(r'^pilot/(?P<pk>\d+)/$',),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', welcomeindex),
    url(r'^/$', welcomeindex),
    url(r'^login/','django.contrib.auth.views.login'),
    url(r'^index/', indexhtml),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pilot/$', pilotpagehtml),
    url(r'^pilot/(?P<pk>\d+)/modify/$',UpdatePilot.as_view(), name="pilot_modify"),
    url(r'^pilot/(?P<pk>\d+)/delete/$',DeleteView.as_view(model=Pilot, success_url="/pilot/",template_name="management/deletePilot.html"), name="pilot_delete"),
    url(r'^pilot/(\w+)', pilotinfohtml),
    url(r'^(\w+)/pilot/(\w+)', pilotinfo),
    url(r'^(\w+)/pilot/', pilotpage),
    url(r'^manufacturer/$',manufacturerpagehtml),
    url(r'^manufacturer/(\w+)',manufacturerinfohtml),
    url(r'^(\w+)/manufacturer/(\w+)',manufacturerinfo),
    url(r'^(\w+)/manufacturer/', pilotpage), 
    url(r'^country/$',countrypagehtml ),
    url(r'^country/(\w+)',countryinfohtml),
    url(r'^(\w+)/country/(\w+)',countryinfohtml),
    url(r'^(\w+)/country/', countrypage),
    url(r'^category/$',categorypagehtml),
    url(r'^category/(\w+)',categoryinfohtml),
    url(r'^(\w+)/category/(\w+)',categoryinfo),
    url(r'^(\w+)/category/', categorypage),
    url(r'^user/', newuser),
    url(r'^user_profile/', profileinfo),
    url(r'^change_password/', changepassword),
    url(r'^change_username/', changeusername),
    url(r'^change_firstname/', changefirstname),
    url(r'^change_secondname/', changesecondname),
    url(r'^change_email/', changeemail),
    url(r'^logout/', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^specialUser/',newuser),
    url(r'^create/new_pilot/$', CreatePilot.as_view(), name='pilot_create'),

)
