from django.db import models

class User(models.Model):

    def __str__(self):
        return self.username

    username = models.CharField(max_length=20, blank=False,verbose_name='User Name')
    password = models.CharField(max_length=30, blank=False,verbose_name='Password')
    ticket = models.CharField(max_length=30, blank=True,null=True)
