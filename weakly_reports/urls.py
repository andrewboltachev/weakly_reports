from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'weakly_reports.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'reports.views.home', name='home'),
    url(r'^week/(?P<year>\d{4})/(?P<week_no>\d+)$', 'reports.views.weekly', name='weekly'),
    url(r'^month/(?P<year>\d{4})/(?P<month_no>\d+)$', 'reports.views.monthly', name='monthly'),
)
