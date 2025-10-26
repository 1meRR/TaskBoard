from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Task

User = get_user_model()


class UserShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')


class TaskSerializer(serializers.ModelSerializer):
    assignee = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    assignee_info = UserShortSerializer(source='assignee', read_only=True)

    class Meta:
        model = Task
        fields = (
            'id',
            'title',
            'description',
            'status',
            'assignee',
            'assignee_info',
            'created_at',
            'updated_at',
        )
        read_only_fields = ('created_at', 'updated_at')
