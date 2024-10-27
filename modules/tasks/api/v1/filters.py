from django_filters import FilterSet
from django_filters import rest_framework as filters
from ...models import Task


class TaskFilter(FilterSet):
    board = filters.NumberFilter(field_name='board_id', lookup_expr='exact')
    
    class Meta:
        model = Task
        fields = ['title', 'description', 'status']

