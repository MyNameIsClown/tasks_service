from django_filters import FilterSet
# from django_filters import rest_framework as filters
from ...models import BoardStatus

class BoardStatusFilter(FilterSet):
    class Meta:
        model = BoardStatus
        fields = ['name', 'board']
