# -*- coding: utf-8 -*-
from django.contrib.auth import login, logout
from django.shortcuts import get_object_or_404
from django.utils.http import is_safe_url
from django.views.generic import FormView, RedirectView

from rest_framework import permissions, renderers, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

# from .forms import *
from .serializers import *


#API Views
class LoginAPIView(APIView):
    """
    ## A API View for user authentication.
    * ## Login (POST)
    url: ^login/$</br>
    url_name: accounts-login</br>
    method: POST</br>
    action: authenticated users</br>
    data:<pre><code>{
        "email": "string",
        "password": "string"
    }
    </code></pre>
    """
    permission_classes = (permissions.AllowAny,)
    renderer_classes = (renderers.JSONRenderer,)
    http_method_names = ['post', 'options']

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.user
        user_serializer = UserSerializer(instance=user)
        (token, created) = Token.objects.get_or_create(user=user)
        response = user_serializer.data.copy()
        response.update({
            'token': token.key
        })

        return Response(response)


class UserAPIViewSet(viewsets.ModelViewSet):
    """
    ## A viewset for viewing and editing user instances.
    * ## List (GET)
    url: ^accounts/$</br>
    url_name: accounts-list</br>
    method: GET</br>
    action: list all users</br>
    data:<pre><code>{
        "links": {
            "next": null,
            "previous": null
        },
        "count": 1,
        "total_pages": 1,
        "results": [{
            "active": boolean,
            "admin": boolean,
            "email": "string",
            "password": "string",
            "superuser": boolean
        }]
    }
    </code></pre>
    * ## Detail (GET)
    url: ^accounts/{pk}/</br>
    method: GET</br>
    action: get user detail</br>
    data:<pre><code>{
        "email":"string",
        "password":"string",
        "active":boolean,
        "admin":boolean,
        "superuser":boolean
    }
    </code></pre>
    * ## Update (PUT)
    url: ^accounts/{pk}/update/</br>
    method: PUT</br>
    action: update user detail</br>
    data:<pre><code>{
        "email":"string",
        "password":"string",
        "active":boolean,
        "admin":boolean,
        "superuser":boolean
    }
    </code></pre>
    * ## Create (POST)
    url: ^accounts/add/</br>
    method: POST</br>
    action: create new user</br>
    data:<pre><code>{
        "email":"string",
        "password":"string",
    }
    </code></pre>
    """
    #set serializer class
    serializer_class = UserSerializer
    #set model scope for queryset
    queryset = BasicUser.objects.all()
