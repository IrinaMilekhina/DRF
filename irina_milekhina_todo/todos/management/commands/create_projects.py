from random import choice, randint, choices

from django.core.management import BaseCommand

from todos.models import Todo, Project
from users.models import User


class Command(BaseCommand):
    help = 'Create todos to test'

    def add_arguments(self, parser):
        parser.add_argument('number', type=int)

    def handle(self, *args, **options):
        number = options['number']
        for i in range(1, number + 1):
            repo_link = f'https://link{i}.com'

            users = User.objects.all()
            users_count = randint(0, len(users))
            users_set = choices(users, k=users_count)

            project = Project.objects.create(name=f'Project name {i}',
                                             repo_link=repo_link)
            print(f'{project} создан')

            for user in users_set:
                project.users.add(user)
