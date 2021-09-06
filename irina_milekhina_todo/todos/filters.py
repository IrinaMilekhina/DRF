from django_filters import rest_framework as filters

from todos.models import Todo, Project


class TodoFilter(filters.FilterSet):
    created = filters.DateFromToRangeFilter()
    updated = filters.DateFromToRangeFilter()

    class Meta:
        model = Todo
        fields = ['created', 'updated']


class ProjectFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Project
        fields = ['name']
