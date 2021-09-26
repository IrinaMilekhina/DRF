from random import choice
from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APITestCase
from rest_framework import status
from todos.models import Project, Todo
from todos.views import ProjectViewSet
from mixer.backend.django import mixer
from users.models import User


# APIRequestFactory
class TestProjectViewSet(TestCase):
    def test_get_list(self):
        # тест проверяет страницу со списком проектов
        factory = APIRequestFactory()
        request = factory.get('/api/projects')
        view = ProjectViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_guest(self):
        # тест проверяет возможность создать новый проект под неавторизованным пользователем
        factory = APIRequestFactory()
        request = factory.post('/api/projects', {'name': 'Тестовый проект', 'repo_link': 'https://testlink.com'},
                               format='json')
        view = ProjectViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_admin(self):
        # тест проверяет возможность создать новый проект под авторизованным пользователем
        factory = APIRequestFactory()
        request = factory.post('/api/projects', {'name': 'Тестовый проект', 'repo_link': 'https://testlink.com'},
                               format='json')
        admin = User.objects.create_superuser('admin', 'admin@amin.com', 'geekbrains')
        force_authenticate(request, admin)
        view = ProjectViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


# APIClient, использование mixer
class TestTodoViewSet(TestCase):
    def test_get_detail(self):
        # тест проверяет страницу с детальной информацией о заметке
        todo = mixer.blend(Todo)
        client = APIClient()
        response = client.get(f'/api/todos/{todo.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_guest(self):
        # тест проверяет возможность редактировать заметку под неавторизованным пользователем
        todo = mixer.blend(Todo)
        client = APIClient()
        response = client.put(f'/api/todos/{todo.id}/',
                              {'text': 'edited test todo', 'project': todo.project.id, 'is_active': True})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


# APITestCase
class TestTodoViewSetAPITestCase(APITestCase):
    def test_get_list(self):
        # тест проверяет страницу со списком заметок
        response = self.client.get('/api/todos/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
