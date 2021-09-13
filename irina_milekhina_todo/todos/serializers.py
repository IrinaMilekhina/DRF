from rest_framework import serializers

from todos.models import Project, Todo
from users.serializers import UserModelSerializer


class ProjectModelSerializer(serializers.ModelSerializer):
    users = UserModelSerializer(many=True)

    class Meta:
        model = Project
        fields = '__all__'


class TodoModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = '__all__'
