from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.views.generic.simple import direct_to_template

from bootstrap.views import home, inside, ajax_example

admin.autodiscover()


urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    
    #Registration
    (r'^accounts/', include('registration.urls')),
    
    (r'^$', home),
    (r'^inside/$', inside),
    (r'^ajax_example', ajax_example),
    
    #Humans and Robots
    ('^humans.txt$', direct_to_template, {'template':'humans.txt', 'mimetype':'text/plain'}),
    ('^robots.txt$', direct_to_template, {'template':'robots.txt', 'mimetype':'text/plain'}),
)
