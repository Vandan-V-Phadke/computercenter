from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'bitsgoacc.views.home', name='home'),
    url(r'^index.html', 'bitsgoacc.views.home'),
    url(r'^audi/', include('audi.urls', namespace='audi')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^ccbook/zone','cclabbooking.views.selectzone'),
    #url(r'^ccbook/details','cclabbooking.views.requestview'),
    url(r'^ccbook/available/(?P<day>\w+)/(?P<month>\w+)/(?P<year>\w+)','cclabbooking.views.show_availability'),
    url(r'^ccbook/admin','cclabbooking.views.admin_view'),
)

urlpatterns += patterns('',(r'^media/(?P<path>.*)$',
    'django.views.static.serve',
    {'document_root': settings.MEDIA_ROOT}))
