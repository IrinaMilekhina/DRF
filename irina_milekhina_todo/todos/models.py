from django.db import models

from users.models import User


class Project(models.Model):
    name = models.CharField(max_length=32)
    repo_link = models.URLField(blank=True)
    users = models.ManyToManyField(User, related_name='projects', related_query_name='project')

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return f'{self.name}_id{self.id}'


class Todo(models.Model):
    text = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE,
                                related_name='todo', related_query_name='todos')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'

    def __str__(self):
        return f'Заметка_id{self.id}'
