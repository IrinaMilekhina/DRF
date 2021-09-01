from rest_framework import serializers

from todos.models import Project, Todo


class ProjectModelSerializer(serializers.HyperlinkedModelSerializer):
    users = serializers.HyperlinkedRelatedField('user-info', many=True, read_only=True)
    todos = serializers.HyperlinkedRelatedField('todo-info', many=True, read_only=True)

    class Meta:
        model = Project
        fields = '__all__'


class TodoModelSerializer(serializers.HyperlinkedModelSerializer):
    project = serializers.HyperlinkedRelatedField('project-info', read_only=True)

    class Meta:
        model = Todo
        fields = '__all__'
