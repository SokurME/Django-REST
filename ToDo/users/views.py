# from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from .models import User
from .serializers import UserModelSerializer
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer


class UserModelViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin, UpdateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
