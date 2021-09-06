from django_filters import rest_framework as filters

from todos.models import Todo


class TodoFilter(filters.FilterSet):
    created = filters.DateFromToRangeFilter()
    updated = filters.DateFromToRangeFilter()

    class Meta:
        model = Todo
        fields = ['created', 'updated']
