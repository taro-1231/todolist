from django.db import models

# Create your models here.

PRIORITY = (('danger','high'),('warning','normal'),('primary','low'))

class TodoModel(models.Model):

    title = models.CharField(max_length=30)
    memo = models.TextField()
    priority = models.CharField(max_length=10,choices = PRIORITY)
    duedate = models.DateField()

    def __str__(self):
        return self.title