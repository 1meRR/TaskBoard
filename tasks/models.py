from django.conf import settings
from django.db import models


class Task(models.Model):
    class Status(models.TextChoices):
        BACKLOG = 'backlog', 'Backlog'
        IN_PROGRESS = 'in_progress', 'В работе'
        DONE = 'done', 'Сделано'

    title = models.CharField('Название', max_length=120)
    description = models.TextField('Описание', blank=True)
    status = models.CharField('Статус', max_length=20, choices=Status.choices, default=Status.BACKLOG)
    assignee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='tasks',
        on_delete=models.CASCADE,
        verbose_name='Исполнитель',
    )
    created_at = models.DateTimeField('Создана', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлена', auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self) -> str:
        return self.title
