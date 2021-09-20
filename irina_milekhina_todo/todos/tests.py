from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework import status
from todos.views import ProjectViewSet


class TestProjectsViewSet(TestCase):
    API_URL = 'http://127.0.0.1:8000/api/projects/'

    def setUp(self):
        self.factory = APIRequestFactory()
        self.new_project = {
            'name': 'Project name 2'
        }
        self.user_data = {
            'username': 'django',
            'email': 'email_django@mail.ru',
            'password': 'geekbrains'
        }

    def test_get_list_guest(self):
        request = self.factory.get(self.API_URL)
        view = ProjectViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_project(self):
        request = self.factory.post(self.API_URL, self.new_project, format='json')
        user = get_user_model().objects.create_superuser(**self.user_data)
        force_authenticate(request, user)
        view = ProjectViewSet.as_view({'post': 'create'})
        response = view(request)
        response.render()
        print(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
