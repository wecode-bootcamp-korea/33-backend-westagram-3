from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length = 20) 
    user_mail = models.CharField(max_length = 20)
    user_password = models.CharField(max_length = 20)
    user_password = models.CharField(max_length = 20)
    user_number = models.CharField(max_length = 15)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    db_table = 'users'
