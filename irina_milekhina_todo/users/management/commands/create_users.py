from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    help = 'Create users to test'

    def add_arguments(self, parser):
        parser.add_argument('number', type=int)

    def handle(self, *args, **options):
        number = options['number']
        for i in range(1, number + 1):
            user = User.objects.create_user(username=f'username{i}',
                                            first_name=f'fname{i}',
                                            last_name=f'lname{i}',
                                            email=f'email{i}@mail.ru',
                                            password='geekbrains')
            print(f'{user} создан')
