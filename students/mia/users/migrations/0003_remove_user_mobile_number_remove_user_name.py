# Generated by Django 4.0.4 on 2022-05-18 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_email_alter_user_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='mobile_number',
        ),
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
    ]
