from django.db import models
from modules.config.models import AuditModel

class Board(AuditModel):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
