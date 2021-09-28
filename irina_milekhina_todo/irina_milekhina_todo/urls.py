from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from todos.views import ProjectViewSet, TodoViewSet
from users.views import UserCustomViewSet

router = DefaultRouter()
router.register('users', UserCustomViewSet)
router.register('projects', ProjectViewSet)
router.register('todos', TodoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    re_path(r'^api/(?P<version>\d\.\d)/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
]
