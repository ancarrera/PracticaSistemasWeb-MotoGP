from django.conf.urls import patterns, include, url
from django.contrib import admin
from appMotoGP.views import *


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'motoGP.views.home', name='home'),
    # url(r'^motoGP/', include('motoGP.foo.urls')),
    #url(r'^pilot/(?P<pk>\d+)/$',),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pilot/$', pilotpage),
    #url(r'^manufacturer/$',manufacturerpage ),
    url(r'^country/$',countrypage ),
    url(r'^category/$',categorypage ),
    url(r'^pilot/(\w+)', pilothtmlinfo),
    url(r'^(\w+)/pilot/(\w+)', pilotinfo),
    url(r'^', index)
    #url(r'^pilot/(\w+)', pilotinfo),
    #url(r'^pilot/', include(admin.site.urls))
    #url(r'^user/(\w+)/$', userpage),
)
