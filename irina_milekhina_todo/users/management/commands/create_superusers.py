from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('username', type=str)

    def handle(self, *args, **options):
        username = options['username']
        user = User.objects.create_superuser(username=f'{username}',
                                             first_name=f'first_name_{username}',
                                             last_name=f'last_name_{username}',
                                             email=f'email_{username}@mail.ru',
                                             password='geekbrains')
        print(f'{user} создан')
