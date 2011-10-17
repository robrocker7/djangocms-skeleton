from django.conf.urls.defaults import *

from django.contrib import admin
from django.conf import settings

from cms.sitemaps import CMSSitemap
from cmsplugin_blog.sitemaps import BlogSitemap

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {
        'sitemaps': {
            'cmspages': CMSSitemap,
            'blogentries': BlogSitemap
        }
    }),
    
    url(r'^', include('cms.urls')),
)

if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns
