from django.db import models
from datetime import date
# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=200, null=False,  blank=False)
    created_at = models.DateField(auto_now_add=True, null=False,  blank=False)  
    deadline = models.DateField(null=False,  blank=False)
    finished_at = models.DateField(null=True)

    class Meta:
        ordering = ['deadline']

    def completed(self):
        if not self.finished_at:
            self.finished_at = date.today()
            self.save()