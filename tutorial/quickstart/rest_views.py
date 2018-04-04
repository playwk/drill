from rest_framework import viewsets
from serializers import UserSerializer, AssetSerializer,ServerSerializer
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
import models