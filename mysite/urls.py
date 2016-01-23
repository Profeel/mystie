from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.views import archive,blog

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)


urlpatterns += patterns('mysite.blog.views',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^blog/', archive),
    url(r'^(?P<blog_id>\d+)/(?P<blog_link>[\w,-]*)$', 'blog', name='blog'),
)