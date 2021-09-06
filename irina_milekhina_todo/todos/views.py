from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet
from todos.filters import TodoFilter
from todos.models import Project, Todo
from todos.serializers import ProjectModelSerializer, TodoModelSerializer


class TodoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectLimitOffsetPagination


class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer
    pagination_class = TodoLimitOffsetPagination
    filterset_class = TodoFilter
