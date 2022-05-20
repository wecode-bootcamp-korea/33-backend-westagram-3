# Generated by Django 4.0.4 on 2022-05-17 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bada', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='allergy',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='allergy_drink',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='drink',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='image',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='nutrition',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='size',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]