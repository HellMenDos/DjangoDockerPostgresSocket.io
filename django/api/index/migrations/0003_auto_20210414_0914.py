# Generated by Django 3.1.4 on 2021-04-14 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_delete_add'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='appleId',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='facebook',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='google',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='location',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='vk',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
