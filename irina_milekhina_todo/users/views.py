from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from users.models import User
from users.serializers import UserModelSerializer, UserModelSerializerWithParams


class UserCustomViewSet(mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        GenericViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.version == '0.2':
            return UserModelSerializerWithParams
        else:
            return UserModelSerializer
