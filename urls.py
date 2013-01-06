from django.conf.urls.defaults import patterns, include, url
from iasstudy_search.views import downloadable
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ias_coaching.views.home', name='home'),
    # url(r'^ias_coaching/', include('ias_coaching.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^downloadable/', downloadable),
)
