from django.conf.urls import include, url
from django.contrib import admin
from polling.views import (
	portal,
    dashboard,
	dashboard_data,
	poll,
)

urlpatterns = [
    # Examples:
    # url(r'^$', 'lectern.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', portal),
    url(r'^poll/$', poll, name='poll'),
    url(r'^dashboard/$', dashboard),
    url(r'^dashboard_data/$', dashboard_data),
    # url(r'^studentlogin/$', studentlogin),
    # url(r'^teacherlogin/$', teacherlogin),

]
