# -*- coding: utf-8 -*-
from django.apps import apps
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import RedirectView

from .views import *

urlpatterns = [
    # app home
    # url(r'^$', RedirectView.as_view(url='/admin')),
    url(r'^$', IndexView.as_view(), name='index'),

    # admin
    url(r'^admin/', admin.site.urls),
]

for app in apps.get_app_configs():
    try:
        urlpatterns += [
            url(
                r'^api/v1/',
                include('{0}.urls'.format(app.name),
                namespace='{0}'.format(app.name))
                ),
        ]
    except:
        pass

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#
admin.site.site_header = 'Digital Signature Manager'
