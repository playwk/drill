from django.shortcuts import render
from django.contrib.auth.models import User
from quickstart import models
from rest_framework import permissions
from rest_framework import serializers
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = User

# Create your views here.
