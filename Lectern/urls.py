from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'lectern.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'polling.views.dashboard'),
    url(r'^poll/$', 'polling.views.poll'),
    url(r'^dashboard/$', 'polling.views.dashboard'),
]
