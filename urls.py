from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

from bootstrap.views import home, inside

admin.autodiscover()


urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    
    #Registration
    (r'^accounts/', include('registration.backends.simple.urls')),
    
    (r'^$', home),
    (r'^inside/$', inside),
)
