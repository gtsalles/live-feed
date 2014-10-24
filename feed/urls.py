from django.conf.urls import patterns, include, url
from django.contrib import admin

from core.urls import router


urlpatterns = patterns('',
    url(r'^$', 'core.views.home', name='home'),
    url(r'^monitor/$', 'core.views.monitor', name='monitor'),
    url(r'^monitor/stats/$', 'core.views.stats', name='stats'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
)