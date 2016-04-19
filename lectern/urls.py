from django.conf.urls import include, url
from django.contrib import admin
from polling.views import (
	portal,
    dashboard,
	dashboard_data,
	poll,
    studentlogin,
    teacherlogin,
)

urlpatterns = [
    # Examples:
    # url(r'^$', 'lectern.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', portal, name='home'),
    url(r'^poll/$', poll, name='poll'),
    url(r'^dashboard/$', dashboard, name="dashboard"),
    url(r'^dashboard_data/$', dashboard_data),
    url(r'^studentlogin/$', studentlogin, name='studentlogin'),
    url(r'^teacherlogin/$', teacherlogin, name='teacherlogin'),

]
