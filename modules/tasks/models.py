from django.db import models
from modules.config.models import AuditModel
from modules.boards.models import Board
class TaskStatus(AuditModel):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Task(AuditModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.ForeignKey(TaskStatus, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
