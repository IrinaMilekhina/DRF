from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from users.models import User
from users.serializers import UserModelSerializer


class UsersViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
