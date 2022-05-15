# from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from .models import Project, TODO
from .serializers import ProjectModelSerializer, TODOModelSerializer
from rest_framework.pagination import LimitOffsetPagination
from .filters import ProjectFilter, TODOFilter
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectLimitOffsetPagination
    filterset_class = ProjectFilter


class TODOLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class TODOModelViewSet(ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOModelSerializer
    pagination_class = TODOLimitOffsetPagination
    filterset_class = TODOFilter

    # filterset_fields = ['project', 'created_at', 'updated_at']

    def perform_destroy(self, request, *args, **kwargs):
        todo = self.get_object()
        todo.is_done = True
        todo.save()
        return Response(status=HTTP_204_NO_CONTENT)
