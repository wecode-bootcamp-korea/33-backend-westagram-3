from django.db import models

# Create your models here.
class User(models.Model):
    name     = models.CharField(max_length = 20)
    mail     = models.CharField(max_length = 50, unique = True)
    password = models.CharField(max_length = 100, unique = True)
    number   = models.CharField(max_length = 15)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    db_table = 'users'