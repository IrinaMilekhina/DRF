from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    help = 'Create users to test'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **options):
        User.objects.all().delete()
        count = options['count']
        for i in range(count):
            user = User.objects.create(username=f'username{i}',
                                       first_name=f'fname{i}',
                                       last_name=f'lname{i}',
                                       email=f'email{i}@mail.ru')
            print(f'user {user} created')
        print('users done')

        # Создаем суперпользователя при помощи менеджера модели
        User.objects.create_superuser('django', 'django@geekshop.local', 'geekbrains')
        print('superuser done')
