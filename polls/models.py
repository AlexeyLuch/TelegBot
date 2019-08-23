from django.db import models
from django.utils import timezone
import datetime

class User_Name(models.Model):
    unique = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.unique


