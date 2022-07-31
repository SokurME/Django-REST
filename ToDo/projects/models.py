from django.db import models
from users.models import User


class Project(models.Model):
    name = models.CharField('Название проекта', max_length=75)
    link = models.URLField('Ссылка на репозиторий', blank=True)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class TODO(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    text = models.TextField('Текст заметки')
    created_at = models.DateField('Дата создания', auto_now_add=True)
    updated_at = models.DateField('Дата обновления', auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_done = models.BooleanField(default=False)
