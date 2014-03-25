from django.conf.urls import patterns, include, url
from django.contrib import admin
from appMotoGP.views import *


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'motoGP.views.home', name='home'),
    # url(r'^motoGP/', include('motoGP.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pilot/$', pilotpage),
    url(r'^manofacturer/$',manofacturerpage ),
    #url(r'^pilot/', include(admin.site.urls))
    #url(r'^user/(\w+)/$', userpage),
)
