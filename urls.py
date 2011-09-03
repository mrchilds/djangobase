from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    
    #(r'^$', include(admin.site.urls)),
    
    #Registration
    (r'^accounts/', include('registration.backends.simple.urls')),
    
    #Bootstrap
    (r'^bootstrap/', include('bootstrap.urls')),

)
