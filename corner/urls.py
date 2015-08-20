from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'corner_front.views.home', name='home'),
    url(r'^add$', 'corner_front.views.add', name='add'),
    url(r'^add/(\d+)/(\d+)/$', 'corner_front.views.add2', name='add2'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
