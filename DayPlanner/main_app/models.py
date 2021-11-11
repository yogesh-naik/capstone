from django.db import models
from django.contrib.auth.models import User

# Create your models here.

TAG_CHOICES = (
    ('personal','PERSONAL'),
    ('family', 'FAMILY'),
)

class Task(models.Model):

    name = models.CharField(max_length=250)
    tag = models.CharField(max_length=10,choices=TAG_CHOICES, default='personal')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    
    
