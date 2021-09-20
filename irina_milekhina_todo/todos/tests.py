from random import choice
from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APITestCase
from rest_framework import status
from todos.models import Project, Todo
from todos.views import ProjectViewSet
from mixer.backend.django import mixer
from users.models import User


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
        self.user = get_user_model().objects.create_superuser(**self.user_data)
        self.client = APIClient()

    def test_get_list_guest(self):
        request = self.factory.get(self.API_URL)
        view = ProjectViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_project(self):
        request = self.factory.post(self.API_URL, self.new_project, format='json')
        force_authenticate(request, self.user)
        view = ProjectViewSet.as_view({'post': 'create'})
        response = view(request)
        response.render()
        print('\ncreate_project', response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_detail_project(self):
        project = mixer.blend(Project)
        self.client.force_authenticate(self.user)
        response = self.client.get(f'{self.API_URL}{project.id}/')
        print('\nget_detail_project', response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_project(self):
        project = mixer.blend(Project)
        print('\nupdate_project', project.name)
        self.client.force_authenticate(self.user)
        response = self.client.put(f'{self.API_URL}{project.id}/', {'name': 'new_project'})
        print('\nupdate_project', response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_project(self):
        projects = mixer.cycle().blend(Project)
        print('\ndelete_project', Project.objects.all())
        self.client.force_authenticate(self.user)
        self.client.delete(f'{self.API_URL}{projects[-1].id}/')
        print('\ndelete_project', Project.objects.all())
        self.assertEqual(len(projects) - 1, len(Project.objects.all()))


class TestTodosViewSet(APITestCase):
    API_URL = 'http://127.0.0.1:8000/api/todos/'

    def setUp(self):
        self.user_data = {
            'username': 'django',
            'email': 'email_django@mail.ru',
            'password': 'geekbrains'
        }
        self.user = get_user_model().objects.create_superuser(**self.user_data)
        self.todos = mixer.cycle().blend(Todo)

    def test_get_list_todos(self):
        self.client.force_authenticate(self.user)
        response = self.client.get(self.API_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_detail_todo(self):
        todo = choice(self.todos)
        self.client.force_authenticate(self.user)
        response = self.client.get(f'{self.API_URL}{todo.id}/')
        print('\nget_detail_todo', response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_todo(self):
        user = choice(User.objects.all())
        project = choice(Project.objects.all())
        self.client.force_authenticate(self.user)
        data = {
            'project': project.id,
            'created_by_user': user.id,
            'text': 'text'
        }
        response = self.client.post(self.API_URL, data)
        print('\ncreate_todo', data)
        print('\ncreate_todo', response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_todo(self):
        todo = choice(Todo.objects.all())
        print('\nupdate_todo', todo.text)
        new_text = 'new text'
        self.client.force_authenticate(self.user)
        response = self.client.put(f'{self.API_URL}{todo.id}/', {'project': todo.project.id, 'text': new_text})
        print('\nupdate_todo', response.content)
        self.assertEqual(Todo.objects.get(id=todo.id).text, new_text)
