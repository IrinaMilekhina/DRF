from django.core.management import BaseCommand

from todos.models import Project


class Command(BaseCommand):

    def handle(self, *args, **options):
        Project.objects.all().delete()