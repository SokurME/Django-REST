from django_filters import rest_framework as filters
from .models import Project, TODO
import django_filters


class ProjectFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Project
        fields = ['name']


class TODOFilter(filters.FilterSet):
    #  project__name = django_filters.CharFilter(lookup_expr='contains')
    created_at = django_filters.DateFilter(field_name='created_at')
    create_at__gt = django_filters.DateFilter(field_name='created_at', lookup_expr='gt')
    created_at__lt = django_filters.DateFilter(field_name='created_at', lookup_expr='lt')

    class Meta:
        model = TODO
        fields = ['project', 'created_at']
