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
    url(r'^api/countries/$', login_required(APICountryList.as_view()), name='country-list'),
    url(r'^api/countries/(?P<pk>\d+)/$', login_required(APICountryDetail.as_view()), name='country-detail'),
    url(r'^api/categories/$', login_required(APICategoryList.as_view()), name='country-list'),
    url(r'^api/categories/(?P<pk>\d+)/$', login_required(APICategoryDetail.as_view()), name='category-detail'),
    url(r'^api/manufacturers/$', login_required(APIManufacturerList.as_view()), name='manufacturer-list'),
    url(r'^api/manufacturers/(?P<pk>\d+)/$', login_required(APIManufacturerDetail.as_view()), name='manufacturer-detail'),
    url(r'^api/pilots/$', login_required(APIPilotList.as_view()), name='pilot-list'),
    url(r'^api/pilots/(?P<pk>\d+)/$', login_required(APIPilotDetail.as_view()), name='pilot-detail'),


    #Web url
    url(r'^$', welcomeindex),
    url(r'^/$', welcomeindex),
    url(r'^accounts/login/','django.contrib.auth.views.login'),
    url(r'^index/', indexhtml),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pilots/(?P<pk>\d+)/reviews/create/$',review, name='review_create'),
    url(r'^pilots/create/$',login_required(CreatePilot.as_view()), name='pilot_create'),
    url(r'^pilots/(?P<pk>\d+)/modify/$',login_required(UpdatePilot.as_view()), name="pilot_modify"),
    url(r'^pilots/(?P<pk>\d+)/delete/$',login_required(DeleteView.as_view(model=Pilot, success_url="/pilots/",template_name="management/deletePilot.html")), name="pilot_delete"),
    url(r'^pilots/(\w+)', pilotinfohtml,name='pilot_detail'),
    url(r'^(\w+)/pilots/(\w+)', pilotinfo, name='pilotinfo'),
    url(r'^(\w+)/pilots/', pilotpage),
    url(r'^pilots/$', pilotpagehtml),
    url(r'^manufacturers/(\w+)',manufacturerinfohtml),
    url(r'^(\w+)/manufacturers/(\w+)',manufacturerinfo),
    url(r'^(\w+)/manufacturers/', pilotpage), 
    url(r'^manufacturers/$',manufacturerpagehtml),
    url(r'^countries/(\w+)',countryinfohtml),
    url(r'^(\w+)/countries/(\w+)',countryinfo),
    url(r'^(\w+)/countries/', countrypage),
    url(r'^countries/$',countrypagehtml ),
    url(r'^categories/(\w+)',categoryinfohtml),
    url(r'^(\w+)/categories/(\w+)',categoryinfo),
    url(r'^(\w+)/categories/', categorypage),
    url(r'^categories/$',categorypagehtml),
    url(r'^user/profile/', profileinfo),
    url(r'^user/changepassword/', changepassword),
    url(r'^user/changeusername/', changeusername),
    url(r'^user/changefirstname/', changefirstname),
    url(r'^user/changesecondname/', changesecondname),
    url(r'^user/changeemail/', changeemail),
    url(r'^user/special/new/',newuser),
    url(r'^user/create/', newuser),
    url(r'^accounts/logout/', 'django.contrib.auth.views.logout', {'next_page': '/'}),
   
  
) 
#static url
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
