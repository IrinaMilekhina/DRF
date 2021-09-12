from django.core.management import BaseCommand

from todos.models import Todo


class Command(BaseCommand):

    def handle(self, *args, **options):
        Todo.objects.all().delete()