from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.views import archive

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
)


urlpatterns = patterns('mysite.blog.views',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', archive),
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    url(r'^(?P<blog_id>\d+)/(?P<blog_link>[\w,-]*)$', 'blog', name='blog'),
)
=======
)
>>>>>>> parent of ce9f02e... Merge pull request #3 from Profeel/1.0
=======
)
>>>>>>> parent of fe0aa71... the 2nd commit
=======
)
>>>>>>> parent of fe0aa71... the 2nd commit
