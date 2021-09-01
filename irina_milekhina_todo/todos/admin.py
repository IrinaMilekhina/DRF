from django.contrib import admin

from todos.models import Project, Todo

admin.site.register(Project)
admin.site.register(Todo)
