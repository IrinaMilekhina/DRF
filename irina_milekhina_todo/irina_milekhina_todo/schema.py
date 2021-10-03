import graphene
from graphene_django import DjangoObjectType

from todos.models import Todo, Project
from users.models import User


class TodoType(DjangoObjectType):
    class Meta:
        model = Todo
        fields = '__all__'


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'projects')


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class Query(graphene.ObjectType):
    all_todos = graphene.List(TodoType)
    all_projects = graphene.List(ProjectType)
    all_users = graphene.List(UserType)
    projects_by_user = graphene.List(ProjectType, name=graphene.String(required=False))

    def resolve_all_projects(self, info):
        return Project.objects.all()

    def resolve_all_todos(self, info):
        return Todo.objects.all()

    def resolve_projects_by_user(self, info, name=None):
        projects = Project.objects.all()
        if name:
            projects = projects.filter(users__first_name=name)
        return projects

schema = graphene.Schema(query=Query)
