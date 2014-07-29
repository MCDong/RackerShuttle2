from django.conf.urls import patterns, include, url
from shuttle import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'RackerShuttle2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^schedule/', views.schedule, name='schedule'),
    url(r'^wait_list/(?P<sid>\d+)', views.wait_list)
)
