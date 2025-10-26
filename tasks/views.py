from django.db.models import Q
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Task.objects.select_related('assignee')
        status_value = self.request.query_params.get('status')
        assignee_id = self.request.query_params.get('assignee')
        search_value = self.request.query_params.get('search')

        if status_value:
            queryset = queryset.filter(status=status_value)
        if assignee_id:
            queryset = queryset.filter(assignee_id=assignee_id)
        if search_value:
            queryset = queryset.filter(
                Q(title__icontains=search_value) | Q(description__icontains=search_value)
            )
        return queryset

    def perform_create(self, serializer):
        serializer.save()
