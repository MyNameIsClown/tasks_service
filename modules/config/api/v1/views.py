from rest_framework import viewsets
from modules.config.models import Status
from modules.config.api.v1.serializers import StatusSerializer

class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer