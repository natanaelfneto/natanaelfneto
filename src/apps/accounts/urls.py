# -*- coding: utf-8 -*-
from django.conf.urls import url

from .views import *


app_name = UserAPIViewSet.__module__.split('.')[0]
urlpatterns = [
    #authenticate user
    # url(
    #     r'^login/$',
    #     LoginAPIView.as_view(), 
    #     name='{0}-login'.format(app_name)
    #     ),
    #get list of all users
    url(
        r'^{0}/$'.format(app_name),
        UserAPIViewSet.as_view({'get': 'list'}),
        name='{0}-list'.format(app_name)
        ),
    #get user detail
    url(
        r'^{0}/(?P<pk>\d+)/$'.format(app_name), 
        UserAPIViewSet.as_view({'get': 'retrieve'}), 
        name='{0}-detail'.format(app_name)
        ),
    #update user detail
    url(
        r'^{0}/(?P<pk>\d+)/update/$'.format(app_name), 
        UserAPIViewSet.as_view({'put': 'update'}), 
        name='{0}-update'.format(app_name)
        ),
    #create new user
    url(
        r'^{0}/add/$'.format(app_name), 
        UserAPIViewSet.as_view({'post': 'create'}), 
        name='{0}-login'.format(app_name)
        ),
]
