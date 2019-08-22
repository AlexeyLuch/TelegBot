from django.db import models

class User_Name(models.Model):
    unique = models.CharField(unique=True,max_length=200,primary_key=1)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.unique

