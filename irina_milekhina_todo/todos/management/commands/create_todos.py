from random import choice

from django.core.management import BaseCommand

from todos.models import Todo, Project


class Command(BaseCommand):
    help = 'Create todos to test'

    def add_arguments(self, parser):
        parser.add_argument('number', type=int)

    def handle(self, *args, **options):
        number = options['number']
        for i in range(1, number + 1):
            text = 'abc ' * i
            project = choice(Project.objects.all())
            todo = Todo.objects.create(text=text,
                                       project=project,
                                       is_active=True)
            print(f'{todo} создан')
