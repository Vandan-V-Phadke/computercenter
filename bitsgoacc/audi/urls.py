from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'audi.views.home', name='home'),
    url(r'^book/$', 'audi.views.book', name='book'),
)
