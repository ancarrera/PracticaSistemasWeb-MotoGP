from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import *
from django.contrib.auth.views import logout
from appMotoGP.views import *
from appMotoGP.forms import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from motoGP import settings


admin.autodiscover()

urlpatterns = patterns('',

    #API urls
    url(r'^api/country/$', login_required(APICountryList.as_view()), name='country-list'),
    url(r'^api/country/(?P<pk>\d+)/$', login_required(APICountryDetail.as_view()), name='country-detail'),
    url(r'^api/category/$', login_required(APICategoryList.as_view()), name='country-list'),
    url(r'^api/category/(?P<pk>\d+)/$', login_required(APICategoryDetail.as_view()), name='category-detail'),
    url(r'^api/manufacturer/$', login_required(APIManufacturerList.as_view()), name='manufacturer-list'),
    url(r'^api/manufacturer/(?P<pk>\d+)/$', login_required(APIManufacturerDetail.as_view()), name='manufacturer-detail'),
    url(r'^api/pilot/$', login_required(APIPilotList.as_view()), name='pilot-list'),
    url(r'^api/pilot/(?P<pk>\d+)/$', login_required(APIPilotDetail.as_view()), name='pilot-detail'),


    #Web url
    url(r'^$', welcomeindex),
    url(r'^/$', welcomeindex),
    url(r'^accounts/login/','django.contrib.auth.views.login'),
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
    url(r'^(\w+)/country/(\w+)',countryinfo),
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
    url(r'^accounts/logout/', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^specialUser/',newuser),
    url(r'^create/new_pilot/$', CreatePilot.as_view(), name='pilot_create'),

) 
#static url
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
