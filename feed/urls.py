from django.conf.urls import patterns, include, url
from django.contrib import admin
from core.views import NoticiasList


urlpatterns = patterns('',
    url(r'^$', NoticiasList.as_view(), name='home'),
    url(r'^monitor/$', 'core.views.monitor', name='monitor'),
    url(r'^monitor/stats/$', 'core.views.stats', name='stats'),
    url(r'^admin/', include(admin.site.urls)),
)