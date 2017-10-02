# -*- coding: utf-8 -*-
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin


urlpatterns = [
	#admin
	url(r'^admin/', admin.site.urls),
	url(r'^', include('common.urls', namespace='common')),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'natanaelfneto'
