from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=2000)
    password = models.CharField(max_length=2000)
    phone = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
            db_table = "users"