from django.db import models
from modules.config.models import AuditModel
from modules.boards.models import Board, BoardStatus

class Task(AuditModel):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    status = models.ForeignKey(BoardStatus, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
