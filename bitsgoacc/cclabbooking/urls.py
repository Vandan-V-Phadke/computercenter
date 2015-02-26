from django.conf.urls.defaults import *

urlpatterns = patterns('myproject.myapp.views',
    (r'^$', 'default_view',
    (r'^something/$', 'something_view',
)