from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status as status_codes

from ...models import Board, BoardStatus
from modules.config.models import DefaultStatus
from .serializers import BoardSerializer, BoardStatusSerializer
from .filters import BoardStatusFilter
from django_filters.rest_framework import DjangoFilterBackend

class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Create default status for the board
        default_status = DefaultStatus.objects.all()
        for status in default_status:
            BoardStatus.objects.create(name=status.name, description=status.description, board=serializer.instance)
        return Response(serializer.data, status=status_codes.HTTP_201_CREATED)
    
class BoardStatusViewSet(viewsets.ModelViewSet):
    queryset = BoardStatus.objects.all()
    serializer_class = BoardStatusSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BoardStatusFilter
