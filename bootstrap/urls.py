from django.conf.urls.defaults import patterns, include, url

from bootstrap.views import bootstrap, inside

urlpatterns = patterns('',
    (r'^example/$', bootstrap),
    (r'^inside/$', inside),
)