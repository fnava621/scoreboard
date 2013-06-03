from django.conf.urls import patterns, include, url
from django.contrib import admin
from scores import views

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', views.home),
    url(r'^(?P<date>\d+)/$', views.date_games_info),
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
