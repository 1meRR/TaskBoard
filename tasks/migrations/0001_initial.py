from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                (
                    'status',
                    models.CharField(
                        choices=[
                            ('backlog', 'Backlog'),
                            ('in_progress', 'В работе'),
                            ('done', 'Сделано'),
                        ],
                        default='backlog',
                        max_length=20,
                        verbose_name='Статус',
                    ),
                ),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создана')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлена')),
                (
                    'assignee',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='tasks',
                        to=settings.AUTH_USER_MODEL,
                        verbose_name='Исполнитель',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
                'ordering': ['-created_at'],
            },
        ),
    ]
