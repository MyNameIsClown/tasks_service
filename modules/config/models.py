from django.db import models
from django.utils import timezone
class AuditModel(models.Model):
    """
    Audit model for all models
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.created_at = timezone.now() if not self.created_at else self.created_at
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

class DefaultStatus(AuditModel):
    """
    Default Status for all boards
    """
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
